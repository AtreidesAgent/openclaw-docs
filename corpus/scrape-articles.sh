# Articles Scrape Script
#!/bin/bash
cd $(dirname $0)
log=log/2026-03-06.md
echo \"$(date): Full articles scrape start\" >> $log
page=1
while : ; do
  urls=$(curl -s "https://neonewstoday.com/author/dylan/page/$page/" | htmlq 'article h2 a' --attribute=href | head -10)
  if [ -z \"$urls\" ]; then echo \"$(date): No more pages at $page\" >> $log; break; fi
  echo \"Page $page: $urls\" >> $log
  page=$((page+1))
  sleep 1
done
