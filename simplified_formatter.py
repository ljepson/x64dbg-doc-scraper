import re

def main():
    """
    Process the x64dbg commands reference file and reformat it for LLM consumption.
    """
    input_file = "x64dbg_commands_reference.md"
    output_file = "x64dbg_commands_reformatted_full.md"
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the original content with reformatted content
    reformatted_content = process_content(content)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(reformatted_content)
    
    print(f"Reformatted content saved to {output_file}")

def process_content(content):
    """
    Process the entire content of the commands reference file.
    """
    # Start with the title
    result = "# x64dbg Command Reference for LLM Consumption\n\n"
    result += "This reference provides information about commands available in x64dbg, formatted for easy consumption by Large Language Models.\n\n"
    
    # Split by categories (## headings)
    categories = re.split(r'##\s+([^\n]+)', content)[1:]  # Skip the title
    
    # Process each category
    for i in range(0, len(categories), 2):
        if i+1 >= len(categories):
            break
            
        category_name = categories[i].strip()
        category_content = categories[i+1].strip()
        
        result += f"## {category_name}\n\n"
        
        # Split the category content into command blocks
        command_blocks = []
        current_block = []
        
        # Skip empty lines at the beginning
        lines = [line for line in category_content.split('\n') if line.strip()]
        
        # Identify command blocks by looking for lines that don't start with spaces, `, or "Response:"
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            # Check if this is a command header line (contains command name and possibly description)
            if ' - ' in line and not line.startswith('`') and not line.startswith('Response:'):
                # If we already have content, save the current block
                if current_block:
                    command_blocks.append(current_block)
                    current_block = []
                
                # Start a new command block
                current_block = [lines[i]]
                
                # Process arguments and response for this command
                j = i + 1
                while j < len(lines) and not (' - ' in lines[j] and not lines[j].strip().startswith('`') and not lines[j].strip().startswith('Response:')):
                    current_block.append(lines[j])
                    j += 1
                
                i = j
                continue
            
            i += 1
        
        # Add the last block if it exists
        if current_block:
            command_blocks.append(current_block)
        
        # Process each command block
        for block in command_blocks:
            if block:
                result += process_command_block(block) + "\n"
    
    return result

def remove_duplicate_text(text):
    """
    Remove duplicated text in descriptions.
    Example: "Memory address. Memory address." becomes "Memory address."
    """
    if not text:
        return text
        
    # Look for duplicated phrases (at least 5 characters long)
    words = text.split()
    if len(words) < 6:  # Too short to have meaningful duplicates
        return text
    
    # Check for exact duplicated phrases
    half_length = len(words) // 2
    first_half = ' '.join(words[:half_length])
    second_half = ' '.join(words[half_length:])
    
    if first_half == second_half:
        return first_half
    
    # Try to find sentences that are repeated
    sentences = re.split(r'[.!?]\s+', text)
    unique_sentences = []
    for sentence in sentences:
        if sentence and sentence not in unique_sentences:
            unique_sentences.append(sentence)
    
    # Check if we've found duplicates
    if len(sentences) > len(unique_sentences):
        return '. '.join(unique_sentences) + ('.' if text.endswith('.') else '')
    
    return text

def process_command_block(block):
    """
    Process a single command block.
    """
    # First line contains command name and description
    first_line = block[0].strip()
    
    # Extract command name and description
    if ' - ' in first_line:
        cmd_parts = first_line.split(' - ', 1)
        command_name = cmd_parts[0].strip()
        description = cmd_parts[1].strip()
    else:
        command_name = first_line
        description = ""
    
    # Handle command aliases
    if '[' in command_name and ']' in command_name:
        # Keep aliases as part of the command name for now
        # We'll handle this in a more sophisticated way if needed
        pass
    
    # Start building the output
    output = f"### Command: {command_name}\n\n"
    
    if description:
        output += f"**Description**: {description}\n\n"
    
    # Extract arguments
    args = []
    for line in block[1:]:
        line = line.strip()
        if line.startswith('`arg') or line.startswith('`[arg'):
            # This is an argument line
            arg_parts = line.split(' - ', 1)
            if len(arg_parts) == 2:
                arg_name = arg_parts[0]
                arg_desc = arg_parts[1].strip()
                # Remove duplicate descriptions
                arg_desc = remove_duplicate_text(arg_desc)
                args.append((arg_name, arg_desc))
        elif line == "Takes no arguments.":
            break
        elif line.startswith('Response:'):
            break
    
    # Build the syntax
    if args:
        # Extract raw argument names for syntax
        arg_names = []
        for arg_name, _ in args:
            # Strip the backticks
            clean_name = arg_name.strip('`')
            arg_names.append(clean_name)
        
        syntax = f"{command_name} {' '.join(arg_names)}"
    else:
        syntax = command_name
    
    output += f"**Syntax**: `{syntax}`\n\n"
    
    # Add arguments section
    if args:
        output += "**Arguments**:\n"
        for arg_name, arg_desc in args:
            output += f"- {arg_name}: {arg_desc}\n"
        output += "\n"
    else:
        output += "**Arguments**: None\n\n"
    
    # Extract response
    response = "None"
    for line in block:
        if line.strip().startswith('Response:'):
            response = line[len('Response:'):].strip()
            # Remove duplicates in response text
            response = remove_duplicate_text(response)
            break
    
    output += f"**Response**: {response}\n\n"
    
    return output

if __name__ == "__main__":
    main() 