import os, re, xml.etree.ElementTree as ET
from html.parser import HTMLParser
from datetime import datetime
from email.utils import parsedate

CORPUS_DIR = os.path.expanduser("~/.openclaw/workspace-business/corpus")
LOG_DIR = os.path.join(CORPUS_DIR, "log")
ART_DIR = os.path.join(CORPUS_DIR, "articles")
INDEX_FILE = os.path.join(CORPUS_DIR, "index.md")
PAGES = range(2, 10)
NS = {"content": "http://purl.org/rss/1.0/modules/content/"}

class HTMLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self._skip = False
    def handle_starttag(self, tag, attrs):
        if tag in ("script","style"): self._skip = True
        if tag in ("p","h1","h2","h3","h4","br"): self.parts.append("\n")
        if tag == "li": self.parts.append("\n- ")
    def handle_endtag(self, tag):
        if tag in ("script","style"): self._skip = False
    def handle_data(self, data):
        if not self._skip: self.parts.append(data)
    def get_text(self):
        text = "".join(self.parts)
        return re.sub(r"\n{3,}", "\n\n", text).strip()

def strip_html(s):
    import html as h
    s = h.unescape(s or "")
    p = HTMLStripper(); p.feed(s); return p.get_text()

def slugify(t):
    t = t.lower()
    t = re.sub(r"[^\w\s-]","",t)
    t = re.sub(r"[\s_]+","-",t)
    return re.sub(r"-+","-",t)[:80].strip("-")

def parse_date(s):
    try:
        t = parsedate(s)
        if t: return datetime(*t[:6]).strftime("%Y-%m-%d")
    except: pass
    return "0000-00-00"

def load_existing_urls():
    urls = set()
    if not os.path.exists(INDEX_FILE): return urls
    with open(INDEX_FILE) as f:
        for line in f:
            urls.update(re.findall(r"https?://[^\s|]+", line))
    return urls

os.makedirs(ART_DIR, exist_ok=True)
existing = load_existing_urls()
print(f"Existing URLs: {len(existing)}")

new_count = skip_count = err_count = 0
index_rows = []

for page in PAGES:
    xml_path = os.path.join(LOG_DIR, f"rss-page-{page}.xml")
    if not os.path.exists(xml_path):
        print(f"Page {page}: missing, skipping"); continue
    try:
        items = ET.parse(xml_path).getroot().findall(".//item")
        print(f"Page {page}: {len(items)} items")
    except ET.ParseError as e:
        print(f"Page {page} error: {e}"); continue

    for item in items:
        try:
            title = (item.findtext("title") or "untitled").strip()
            url = (item.findtext("link") or "").strip()
            pubdate = (item.findtext("pubDate") or "").strip()
            cats = [c.text.strip() for c in item.findall("category") if c.text]
            encoded = item.findtext("content:encoded", namespaces=NS) or item.findtext("description") or ""
            if not url: continue
            if url in existing: skip_count += 1; continue
            date_str = parse_date(pubdate)
            slug = slugify(title)
            fname = f"{date_str}-{slug}.md"
            fpath = os.path.join(ART_DIR, fname)
            if os.path.exists(fpath): fname = f"{date_str}-{slug}-2.md"; fpath = os.path.join(ART_DIR, fname)
            tags = ", ".join(cats)
            content = strip_html(encoded)
            md = f"""---
title: "{title.replace('"',"'")}"
date: {date_str}
url: {url}
tags: [{tags}]
source: neonewstoday
---

# {title}

**Published:** {pubdate}
**URL:** {url}
**Tags:** {tags}

---

{content}
"""
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(md)
            existing.add(url)
            new_count += 1
            index_rows.append(f"| {title[:60]} | {date_str} | {url} | neonewstoday | {tags[:40]} | articles/{fname} |\n")
        except Exception as e:
            err_count += 1
            print(f"  Error: {e}")

if index_
