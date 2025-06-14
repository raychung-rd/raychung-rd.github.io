#!/usr/bin/env python3
import bibtexparser
import os
import re
from datetime import datetime

def clean_title(title):
    """Clean the title for use in filenames."""
    # Remove LaTeX commands and special characters
    title = re.sub(r'\\[a-zA-Z]+{.*?}', '', title)
    title = re.sub(r'[{}]', '', title)
    # Replace spaces with hyphens and remove special characters
    title = re.sub(r'[^a-zA-Z0-9\s-]', '', title)
    title = title.strip().replace(' ', '-')
    return title

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

    # Create the markdown content
    md = f"""---
title: "{entry['title']}"
collection: publications
category: {category}
permalink: /publication/{date}-{clean_title_text}
date: {date}
venue: '{entry.get('journal', entry.get('booktitle', 'Unknown venue'))}'
"""

    # Add paper URL if available
    if 'url' in entry:
        md += f"paperurl: '{entry['url']}'\n"

    # Add citation
    authors = entry.get('author', '').replace(' and ', ', ')
    citation = f"{authors}. ({year}). {entry['title']}. {entry.get('journal', entry.get('booktitle', ''))}."
    md += f"citation: '{citation}'\n"

    md += "---\n\n"

    # Add abstract if available
    if 'abstract' in entry:
        md += f"{entry['abstract']}\n\n"

    # Add link to paper
    if 'url' in entry:
        md += f"[Access paper here]({entry['url']}){{:target=\"_blank\"}}\n"
    else:
        md += f"Use [Google Scholar](https://scholar.google.com/scholar?q={clean_title_text.replace('-', '+')}){{:target=\"_blank\"}} for full citation\n"

    return filename, md

def main():
    # Read the BibTeX file
    with open('publications.bib', 'r', encoding='utf-8') as bibtex_file:
        parser = bibtexparser.bparser.BibTexParser(common_strings=True)
        bib_database = bibtexparser.load(bibtex_file, parser=parser)

    # Create _publications directory if it doesn't exist
    os.makedirs('../_publications', exist_ok=True)

    # Process each entry
    for entry in bib_database.entries:
        try:
            filename, content = create_markdown(entry)
            with open(f"../_publications/{filename}", 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Successfully created: {filename}")
        except Exception as e:
            print(f"Error processing entry: {entry.get('title', 'Unknown')}")
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 