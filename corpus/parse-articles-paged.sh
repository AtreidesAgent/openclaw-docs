#!/bin/bash
cd $(dirname $0)
log=log/2026-03-06-paged-run.md
echo "$(date): Paged RSS parse start (pages 2-9)" >> $log
existing=$(grep -o 'https://neonewstoday.com/[^ |]*' index.md | sort | uniq)
count_new=0
for page in {2..9}; do
  rss_url="https://neonewstoday.com/author/dylan/feed/?paged=$page"
  curl -s "$rss_url" > "log/rss-page-$page.xml"
  items=$(xmlstarlet sel -t -v "count(//item)" log/rss-page-$page.xml 2>/dev/null || echo 0)
  echo "Page $page: $items items" >> $log
  n=0
  xmlstarlet sel -t -m "//item" -v "concat(title,'|',link,'|',pubDate,'|',string-join(category, ', '),'|',translate(content:encoded, '&#10;&#13;&quot;&lt;&gt;', ' \n\n\"<>'))" -n log/rss-page-$page.xml | while IFS='|' read -r title link pubdate cats content; do
    slug=$(echo "$link" | sed 's|.*/||; s/[ /:]/-/g; s/--+/-/g')
    date_slug=$(echo "$pubdate" | sed 's/ .*//; s/-/ /g' | cut -d' ' -f1-3 | tr ' ' '-' | sed 's/-//2g')
    file="articles/${date_slug}-${slug}.md"
    url_slug=$(echo "$link" | sed 's|https://neonewstoday.com/||')
    if ! echo "$existing" | grep -q "$url_slug"; then
      cat > "$file" << MD
---
title: $title
date: $pubdate
url: $link
tags: [$cats]
source: neonewstoday
---
# $title

$content
MD
      ((count_new++))
      echo "| $title | $pubdate | $link | neonewstoday | $cats | $file |" >> index.md.tmp
      echo "{\"title\":\"$title\",\"url\":\"$link\",\"date\":\"$pubdate\",\"tags\":[\"$cats\"]}" >> articles/index.json.tmp
    fi
    ((n++))
  done
done
mv index.md.tmp index.md
mv articles/index.json.tmp articles/index.json || touch articles/index.json
echo "$(date): Added $count_new new articles. Total files: $(ls articles/*.md | wc -l)" >> $log
