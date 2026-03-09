#!/usr/bin/env python3
import xml.etree.ElementTree as ET
import re
from html import unescape
from datetime import datetime
import os
import glob
from pathlib import Path

NS = {
    'content': 'http://purl.org/rss/1.0/modules/content/',
    'dc': 'http://purl.org/dc/elements/1.1/'
}

def slugify(title):
    slug = re.sub(r'[^\w\s-]', '', title.lower()).strip()
    slug = re.sub(r'[\s_-]+', '-', slug).strip('-')
    return slug[:100]

def clean_html(text):
    text = unescape(text)
    text = re.sub(r'<[^>]*>', '', text)  # strip tags
    text = re.sub(r'\s+', ' ', text)  # normalize space
    return text.strip()

# Read existing URLs
existing_urls = set()
index_path = 'index.md'
if os.path.exists(index_path):
    with open(index_path, 'r') as f:
        for line in f:
            if 'https://neonewstoday.com' in line:
                url = re.search(r'https://neonewstoday\.com[^\s|]*', line)
                if url:
                    existing_urls.add(url.group(0))

new_entries = []
log = 'log/2026-03-06-python-parse.md'
with open(log, 'w') as logf:
    logf.write(f"{datetime.now()}: Starting parse pages 2-9\n")

for page_file in sorted(glob.glob('log/rss-page-[2-9].xml')):
    page = page_file.split('-')[-1].replace('.xml', '')
    tree = ET.parse(page_file)
    root = tree.getroot()
    items = root.findall('.//item')
    logf.write(f"Page {page}: {len(items)} items\n")
    for item in items:
        title_elem = item.find('title')
        title = title_elem.text.strip() if title_elem is not None else 'No title'
        link_elem = item.find('link')
        link = link_elem.text.strip() if link_elem is not None else ''
        pubdate_elem = item.find('pubDate')
        pubdate = pubdate_elem.text.strip() if pubdate_elem is not None else ''
        cats = []
        for cat in item.findall('category'):
            cats.append(cat.text.strip())
        tags = ', '.join(cats) if cats else ''
        content_elem = item.find('content:content', NS)
        content_html = content_elem.text if content_elem is not None else ''
        content_md = clean_html(content_html)
        
        if link in existing_urls:
            continue
        
        # Slug and date
        dt = datetime.strptime(pubdate.split()[1:4], '%d %b %Y') if pubdate else datetime.now()
        date_slug = dt.strftime('%Y-%m-%d')
        slug = slugify(title)
        filename = f"articles/{date_slug}-{slug}.md"
        
        yaml = f"""---
title: {title}
date: {pubdate}
url: {link}
tags: [{tags}]
source: neonewstoday
---
"""
        md_content = f"# {title}\n\n{content_md}"
        with open(filename, 'w') as f:
            f.write(yaml + md_content)
        
        path_rel = filename
        new_entries.append(f"| {title} | {pubdate} | {link} | neonewstoday | {tags} | {path_rel} |")
        logf.write(f"Added: {title[:50]}...\n")
    
    logf.write(f"Page {page} done.\n")

# Append to index.md
with open(index_path, 'a') as f:
    f.write("\n## New Articles (Paged)\n")
    for entry in new_entries:
        f.write(entry + "\n")

print(f"Added {len(new_entries)} new articles. Total MD files: {len(glob.glob('articles/*.md'))}")
