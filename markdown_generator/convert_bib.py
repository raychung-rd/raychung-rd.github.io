#!/usr/bin/env python3
import bibtexparser
import os
import re
from datetime import datetime

def format_single_author(author_full_name):
    """Format a single author's name from 'Lastname, Firstname' to 'Firstname Lastname'."""
    parts = [p.strip() for p in author_full_name.split(',')]
    if len(parts) == 2:
        return f"{parts[1]} {parts[0]}"
    return author_full_name # Return as is if not in 'Last, First' format

def format_authors_list(authors_string):
    """Format a list of authors, converting each from 'Lastname, Firstname' to 'Firstname Lastname'."""
    individual_authors = [a.strip() for a in authors_string.split(' and ')]
    formatted_authors = [format_single_author(author) for author in individual_authors]
    return ", ".join(formatted_authors)

def clean_title(title):
    """Clean the title for use in filenames."""
    # Remove LaTeX commands and special characters
    title = re.sub(r'\\[a-zA-Z]+{.*?}', '', title)
    title = re.sub(r'[{}]', '', title)
    # Replace spaces with hyphens and remove special characters
    title = re.sub(r'[^a-zA-Z0-9\s-]', '', title)
    title = title.strip().replace(' ', '-')
    return title

def get_author_position(authors, target_author="Chung"):
    """Determine if the target author is first or second author."""
    author_list = [a.strip() for a in authors.split(' and ')]
    for i, author in enumerate(author_list):
        if target_author.lower() in author.lower():
            if i == 0:
                return "first"
            elif i == 1:
                return "second"
    return "other"

def get_category(entry_type):
    """Determine the category based on entry type."""
    if entry_type.lower() in ['article', 'journal']:
        return 'manuscripts'
    elif entry_type.lower() in ['inproceedings', 'conference']:
        return 'conferences'
    else:
        return 'manuscripts'  # default to manuscripts

def create_markdown(entry):
    """Create markdown content for a publication."""
    # Get the date
    if 'year' in entry:
        year = entry['year']
        month = entry.get('month', '01')
        day = entry.get('day', '01')
        
        # Convert month name to number if needed
        if month.isalpha():
            try:
                month = datetime.strptime(month[:3], '%b').month
            except ValueError:
                month = 1
        month = f"{int(month):02d}"
        day = f"{int(day):02d}"
        
        date = f"{year}-{month}-{day}"
    else:
        date = "1900-01-01"

    # Clean the title for the filename
    clean_title_text = clean_title(entry['title'])
    filename = f"{date}-{clean_title_text}.md"

    # Get the category
    category = get_category(entry.get('ENTRYTYPE', 'article'))

    # Get author position
    authors = entry.get('author', '')
    author_position = get_author_position(authors)

    # Format authors for markdown output
    formatted_authors_for_md = format_authors_list(authors)

    # Create the markdown content
    md = f"""---
title: "{entry['title']}"
collection: publications
category: {category}
permalink: /publication/{date}-{clean_title_text}
date: {date}
venue: '{entry.get('journal', entry.get('booktitle', 'Unknown venue'))}'
authors: '{formatted_authors_for_md}'
author_position: '{author_position}'
"""

    # Add paper URL if available
    if 'url' in entry:
        md += f"paperurl: '{entry['url']}'\n"
    elif 'doi' in entry:
        md += f"paperurl: 'https://doi.org/{entry['doi']}'\n"

    # Add citation
    citation = f"{entry.get('volume', '')}({entry.get('number', '')}), {entry.get('pages', '')}"
    md += f"citation: '{citation}'\n"

    md += "---\n\n"

    # Add abstract if available
    if 'abstract' in entry:
        md += f"{entry['abstract']}\n\n"

    # Add link to paper
    if 'url' in entry:
        md += f"[Access paper here]({entry['url']}){{:target=\"_blank\"}}\n"
    elif 'doi' in entry:
        md += f"[Access paper here](https://doi.org/{entry['doi']}){{:target=\"_blank\"}}\n"

    return filename, md

def main():
    # Read the BibTeX file
    bibtex_path = os.path.join(os.path.dirname(__file__), 'publications.bib')
    with open(bibtex_path, 'r', encoding='utf-8') as bibtex_file:
        parser = bibtexparser.bparser.BibTexParser(common_strings=True)
        bib_database = bibtexparser.load(bibtex_file, parser=parser)

    # Create _publications directory if it doesn't exist
    output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), '_publications')
    os.makedirs(output_dir, exist_ok=True)

    # Process each entry
    for entry in bib_database.entries:
        try:
            filename, content = create_markdown(entry)
            output_path = os.path.join(output_dir, filename)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Successfully created: {filename}")
        except Exception as e:
            print(f"Error processing entry: {entry.get('title', 'Unknown')}")
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 