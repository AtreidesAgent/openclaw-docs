import os, re, xml.etree.ElementTree as ET
from html.parser import HTMLParser
from datetime import datetime
from email.utils import parsedate

CORPUS_DIR = "/Users/dylansagent/.openclaw/workspace-business/corpus"
LOG_DIR = os.path.join(CORPUS_DIR, "log")
ART_DIR = os.path.join(CORPUS_DIR, "articles")
INDEX_FILE = os.path.join(CORPUS_DIR, "index.md")
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
    # Also check articles directory
    if os.path.exists(ART_DIR):
        for fname in os.listdir(ART_DIR):
            if fname.endswith('.md'):
                try:
                    with open(os.path.join(ART_DIR, fname)) as f:
                        content = f.read()
                        m = re.search(r"^url:\s*(.+)$", content, re.MULTILINE)
                        if m: urls.add(m.group(1).strip())
                except: pass
    return urls

os.makedirs(ART_DIR, exist_ok=True)
existing = load_existing_urls()
print(f"Loaded {len(existing)} existing URLs")

new_count = skip_count = err_count = 0
index_rows = []

# Process page 1 RSS
xml_path = os.path.join(LOG_DIR, "rss-page-1.xml")
if not os.path.exists(xml_path):
    print(f"Error: {xml_path} not found")
    exit(1)

try:
    items = ET.parse(xml_path).getroot().findall(".//item")
    print(f"Found {len(items)} items in RSS")
except ET.ParseError as e:
    print(f"Parse error: {e}")
    exit(1)

for item in items:
    try:
        title = (item.findtext("title") or "untitled").strip()
        url = (item.findtext("link") or "").strip()
        pubdate = (item.findtext("pubDate") or "").strip()
        cats = [c.text.strip() for c in item.findall("category") if c.text]
        encoded = item.findtext("content:encoded", namespaces=NS) or item.findtext("description") or ""
        if not url: continue
        if url in existing: 
            skip_count += 1
            continue
        date_str = parse_date(pubdate)
        slug = slugify(title)
        fname = f"{date_str}-{slug}.md"
        fpath = os.path.join(ART_DIR, fname)
        if os.path.exists(fpath): 
            fname = f"{date_str}-{slug}-2.md"
            fpath = os.path.join(ART_DIR, fname)
        tags = ", ".join(cats) if cats else "General"
        content = strip_html(encoded)
        md = f"""---
title: "{title.replace('"','\\"')}"
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
        index_rows.append((title, date_str, url, tags, fname))
        print(f"  [NEW] {title[:60]}...")
    except Exception as e:
        err_count += 1
        print(f"  Error processing item: {e}")

# Update log
log_path = os.path.join(LOG_DIR, datetime.now().strftime("%Y-%m-%d-corpus-update.md"))
with open(log_path, "w") as f:
    f.write(f"""# Corpus Update Log - {datetime.now().isoformat()}

## Articles
- New: {new_count}
- Skipped (duplicates): {skip_count}
- Errors: {err_count}

## New Articles
""")
    for title, date_str, url, tags, fname in index_rows:
        f.write(f"- [{title}](articles/{fname})\n")

print(f"\nDone: {new_count} new articles, {skip_count} skipped, {err_count} errors")
print(f"Log written to {log_path}")
