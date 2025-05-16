import requests
from bs4 import BeautifulSoup
import urllib.parse
import time
import re
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

# Base URL for the documentation
BASE_URL = "https://help.x64dbg.com/en/latest/"

# Starting page as per your link (which contains links to categories)
COMMANDS_MAIN_PAGE = "https://help.x64dbg.com/en/latest/commands/index.html"

# Rate limiting between requests (seconds)
REQUEST_DELAY = 1

# Maximum workers for parallel processing
MAX_WORKERS = 4

# Configure this to control how much information to include
INCLUDE_EXAMPLES = True

def get_soup(url):
    """Fetches a URL and returns a BeautifulSoup object, or None on error."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        return BeautifulSoup(response.content, 'html.parser')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_category_links(main_page_url):
    """
    Extracts links to command category pages from the main commands page.
    Tries multiple approaches to find categories.
    """
    print(f"Extracting category links from: {main_page_url}")
    soup = get_soup(main_page_url)
    if not soup:
        return []

    categories = []
    
    # Try method 1: Check sidebar navigation
    nav_menu = soup.select_one("nav.wy-nav-side div.wy-menu-vertical")
    if not nav_menu:
        nav_menu = soup.select_one("div.wy-menu-vertical")

    if nav_menu:
        for link_tag in nav_menu.find_all('a', class_='reference', href=True):
            href = link_tag['href']
            full_url = urllib.parse.urljoin(main_page_url, href)

            if "/commands/" in full_url and full_url.endswith('index.html'):
                category_name = link_tag.get_text(strip=True)
                if category_name and category_name != "Commands":
                    categories.append({'name': category_name, 'url': full_url})
    
    # Try method 2: Check main content area for a table of contents
    if not categories:
        main_content = soup.select_one("div.toctree-wrapper li")
        if main_content:
            for link_tag in main_content.find_all('a', href=True):
                href = link_tag['href']
                if href.endswith('/') and not href.startswith(('#', 'http', '../')) and "index.html" not in href:
                    full_url = urllib.parse.urljoin(main_page_url, href)
                    category_name = link_tag.get_text(strip=True)
                    if category_name:
                        categories.append({'name': category_name, 'url': full_url})
    
    # Deduplicate categories by URL
    unique_categories = list({cat['url']: cat for cat in categories}.values())

    print(f"Found {len(unique_categories)} unique category links.")

    return unique_categories

def extract_command_links_from_category(category_url):
    """
    Extracts links to individual command pages from a category page.
    """
    soup = get_soup(category_url)
    if not soup:
        return []

    command_links = []
    main_content = soup.select_one(".compound.toctree-wrapper")
    if not main_content:
        main_content = soup

    # Look for command links in the main content
    for link_tag in main_content.find_all('a', class_='reference internal', href=True):
        href = link_tag['href']
        if href.endswith('.html') and not href.startswith(('#', 'http', '../')):
            command_name_text = link_tag.get_text(strip=True)
            
            # Extract primary command name
            command_parts = command_name_text.split('/')
            primary_command_name = command_parts[0].strip()
            full_url = urllib.parse.urljoin(category_url, href)

            command_links.append({
                'name': primary_command_name,
                'url': full_url
            })

    # Deduplicate command links by URL
    unique_command_links = list({cmd['url']: cmd for cmd in command_links}.values())

    return unique_command_links

def extract_command_details(command_url, command_info):
    """
    Extracts and formats details for a single command.
    """
    soup = get_soup(command_url)
    if not soup:
        return None

    details = {
        'name': command_info['name'],
        'aliases': [], 
        'description': 'Description not found.',
        'syntax': f'{command_info["name"]} [arguments...]',
        'result': None,
        'example': None
    }

    main_content = soup.select_one(".section")
    if not main_content:
        main_content = soup

    # Extract Command Name from H1
    h1_tag = main_content.find('h1')
    if h1_tag:
        raw_name = h1_tag.get_text(strip=True).replace('¶', '').strip()
        name_parts = raw_name.split('/')
        details['name'] = name_parts[0].strip()
        if len(name_parts) > 1:
            details['aliases'] = [part.strip() for part in name_parts[1:] if part.strip()]

    # Extract Description
    current_element = h1_tag
    if current_element:
        for sibling in current_element.find_next_siblings():
            if sibling.name == 'p':
                desc_text = sibling.get_text(strip=True)
                if desc_text and len(desc_text) > 10:
                    details['description'] = desc_text
                    break
            if sibling.name in ['h2', 'h3', 'div', 'section']:
                break

    # Extract Syntax/Arguments
    details['syntax'] = parse_arguments(soup)

    # Extract Result
    details['result'] = parse_result(soup)

    # Extract Example if configured to include them
    if INCLUDE_EXAMPLES:
        example_heading = main_content.find(['h2', 'h3'], string=re.compile(r'Example|Examples', re.IGNORECASE))
        if example_heading:
            next_elem = example_heading.find_next_sibling()
            if next_elem and next_elem.name == 'pre':
                details['example'] = next_elem.get_text(strip=True)
            elif next_elem and next_elem.name == 'div' and next_elem.select_one('pre'):
                details['example'] = next_elem.select_one('pre').get_text(strip=True)

    return details

def format_command_details(details):
    """Format command details into a markdown string."""
    lines = []
    
    # Command name and description
    if details['name'] and details['description']:
        lines.append(f"{details['name']} - {details['description']}")
    elif details['name']:
        lines.append(f"{details['name']}")
    
    # Format syntax as a separate line if it exists
    if details.get('syntax') and details['syntax'] != "This command has no arguments.":
        lines.append("")
        lines.append(details['syntax'])
    elif details.get('syntax') == "This command has no arguments.":
        lines.append("")
        lines.append("Takes no arguments.")
    
    # Format result
    if details.get('result') and details['result'] != "None":
        lines.append("")
        lines.append(f"Response: {details['result']}")
    else:
        lines.append("")
        lines.append("Response: None")
    
    # Return the formatted string
    return "\n".join(lines)

def process_category(category):
    """Process all commands in a category."""
    command_links = extract_command_links_from_category(category['url'])
    if not command_links:
        return f"\n## {category['name']}\n\n_No commands found for this category._\n"
    
    results = [f"\n## {category['name']}\n"]
    
    for cmd_link in command_links:
        time.sleep(REQUEST_DELAY)  # Be polite to the server
        details = extract_command_details(cmd_link['url'], cmd_link)
        if details:
            results.append(format_command_details(details) + "\n")
        else:
            results.append(f"{cmd_link['name']} - _Could not extract details._\n\n")
    
    return "\n".join(results)

def parse_arguments(soup):
    """Parse the arguments section from the command documentation."""
    arguments_section = soup.find("div", {"class": "section", "id": "arguments"})
    if not arguments_section:
        return "This command has no arguments."

    # Find all paragraphs in the arguments section
    arg_paragraphs = arguments_section.find_all("p")
    
    if not arg_paragraphs:
        return "This command has no arguments."
    
    arguments = []
    for p in arg_paragraphs:
        # Find the code element containing the argument name
        arg_code = p.find("code", {"class": "docutils literal"})
        if not arg_code:
            continue
            
        # Extract the argument name and preserve brackets for optional args
        arg_name = arg_code.get_text(strip=True)
        
        # Get the description text - everything after the code element
        # We need to reconstruct it with any inline code elements preserved
        description = ""
        next_elem = arg_code.next_sibling
        
        # Skip to the actual text content (there might be a </code> tag between)
        while next_elem and not next_elem.string:
            next_elem = next_elem.next_sibling
            
        if next_elem:
            # Start with the first text node
            description = next_elem.string.strip() if next_elem.string else ""
            
        # Process the remaining elements to preserve inline code blocks
        for elem in p.contents[p.contents.index(arg_code) + 1:]:
            if elem.name == "code":
                # Preserve inline code blocks with backticks
                description += f" `{elem.get_text(strip=True)}`"
            elif elem.string:
                description += elem.string
                
        # Clean and format the description
        description = re.sub(r'\s+', ' ', description).strip()
        
        # Format the argument entry
        arguments.append(f"`{arg_name}` - {description}")
    
    return "\n".join(arguments) if arguments else "This command has no arguments."

def parse_result(soup):
    """Parse the result section from the command documentation."""
    result_section = soup.find("div", {"class": "section", "id": "result"})
    if not result_section:
        return "None"
    
    # Get all paragraphs in the result section
    result_paragraphs = result_section.find_all("p")
    
    if not result_paragraphs:
        return "None"
    
    result_text = ""
    
    for p in result_paragraphs:
        # Process each paragraph, preserving inline code blocks
        paragraph_text = ""
        
        for elem in p.contents:
            if elem.name == "code":
                # Preserve inline code blocks with backticks
                paragraph_text += f"`{elem.get_text(strip=True)}`"
            elif elem.string:
                paragraph_text += elem.string
                
        # Clean and format the paragraph text
        paragraph_text = re.sub(r'\s+', ' ', paragraph_text).strip()
        result_text += paragraph_text + " "
    
    return result_text.strip() if result_text else "None"

def main():
    """Main function to orchestrate the scraping."""
    markdown_lines = ["# x64dbg Command Reference\n"]
    
    categories = extract_category_links(COMMANDS_MAIN_PAGE)
    if not categories:
        print("No categories found. The script might need updated selectors.")
        return
    
    total_categories = len(categories)
    print(f"Processing {total_categories} categories...")
    
    # Process each category with progress tracking
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_to_category = {executor.submit(process_category, category): category for category in categories}
        
        for i, future in enumerate(as_completed(future_to_category), 1):
            category = future_to_category[future]
            try:
                result = future.result()
                markdown_lines.append(result)
                print(f"[{i}/{total_categories}] Processed category: {category['name']}")
            except Exception as e:
                print(f"[{i}/{total_categories}] Error processing {category['name']}: {e}")
    
    output_filename = "x64dbg_commands_reference.md"
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write("".join(markdown_lines))
    
    print(f"\nScraping complete. Output saved to {output_filename}")

if __name__ == "__main__":
    main()