# x64dbg Documentation Scraper

A tool for extracting and formatting [x64dbg](https://x64dbg.com/) command documentation for use with Large Language Models (LLMs).

## Overview

This project provides tools to scrape the official x64dbg documentation website and format the commands reference in a way that's optimized for consumption by LLMs. This enables AI tools to better understand x64dbg commands and provide more accurate assistance for reverse engineering and debugging tasks.

## Features

- **Web Scraping**: Automatically extracts command documentation from the x64dbg help website
- **Formatting**: Reformats the documentation in a clean, consistent structure
- **Duplicate Removal**: Eliminates duplicated text often found in the original documentation
- **LLM Optimization**: Structures data in a way that's easy for language models to parse

## Files

- `scrape_x64dbg_docs.py`: Script that scrapes the x64dbg documentation and creates the initial reference file
- `simplified_formatter.py`: Script that reformats the scraped documentation for better LLM consumption
- `x64dbg_commands_reference.md`: The raw scraped documentation
- `x64dbg_commands_reformatted_full.md`: The final formatted documentation optimized for LLMs

## Why This Is Useful

When working with x64dbg through AI tools or LLM-powered assistants, having properly formatted documentation allows for:

1. More accurate command suggestions
2. Better explanation of command arguments and syntax
3. Improved ability for AI to help with debugging tasks
4. Reduced hallucinations in AI responses about x64dbg functionality

## Usage

### Running the Scraper

```bash
python scrape_x64dbg_docs.py
```

This will create the initial `x64dbg_commands_reference.md` file.

### Formatting the Documentation

```bash
python simplified_formatter.py
```

This will generate the LLM-optimized `x64dbg_commands_reformatted_full.md` file.

## Requirements

- Python 3.6+
- BeautifulSoup4
- Requests

## License

See the [LICENSE](LICENSE) file for details.
