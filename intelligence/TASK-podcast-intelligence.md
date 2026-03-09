# TASK-podcast-intelligence.md

## Podcast: On The Brink with Castle Island
- **Hosts:** Nic Carter & Matt Walsh
- **Channel:** https://www.youtube.com/@OnTheBrinkwithCastleIsland
- **Release Schedule:** Thursdays (check Fridays)
- **Purpose:** Weekly market/blockchain intelligence for research focus & news comparison

## Collection Protocol

### Weekly Cadence — Weekly Roundup ONLY
- **Check:** Every Friday via cron
- **Filter:** Title contains "Weekly Roundup" (skip guest interviews)
- **Action:** Download new episode transcript
- **Location:** `intelligence/weekly/transcripts/`
- **Naming:** `onthebrink-YYYY-MM-DD.txt`

**Note:** Full catalog exists for historical context (Jan-Mar 2026), but ongoing collection is **Weekly Roundup episodes only**.

### Daily Briefings — Crypto Market Briefing
- **Source:** Existing "Crypto Market Briefing" cronjob output
- **Output:** `intelligence/daily/YYYY-MM-DD.md`
- **Format:** Date, headlines, key developments, brief take per story

## Analysis Tasks

### 1. Theme Cataloging
Track recurring themes per episode:
- DeFi/aDeFi/L1-L2 scaling
- Bitcoin/Ethereum developments
- Institutional adoption/ETFs
- Policy/regulatory moves
- VC/crypto markets
- Macro/global context

Store in: `intelligence/themes/` by episode date

### 2. Weekly Delta Analysis
After each Weekly Roundup episode, generate:
`intelligence/compare/deltas/week-of-YYYY-MM-DD.md`

Sections:
- **Daily Headlines (Mon-Thu):** What was covered in morning briefings
- **Podcast Focus:** What Nic & Matt emphasized
- **Gaps:** Daily miss, podcast flags as big
- **Confirmations:** Both sources agree
- **Contradictions:** Daily said X, podcast says Y
- **Actionable Insights:** Research priorities for next week

### 3. Long-term Theme Tracking
Maintain running list of:
- Recurring topics worth deep dives
- Hypotheses to validate
- Narrative shifts week-to-week
- Sources mentioned

## Priority Research Themes
(as specified by Dylan)
- TBD: will update as patterns emerge

## Cron Configuration
```
pm-fridays: fetch-onthebrink-roundup
- Fetch channel playlist from YouTube
- Filter: title matches "Weekly Roundup"
- Download transcript for latest
- Store: intelligence/weekly/transcripts/
- Trigger: delta analysis generation
```

---

## Post-Scrape Cleaning (REQUIRED)

A transcript cleaning script is installed at:
`~/.openclaw/workspace-business/clean_transcripts.py`

**Every time you download a new On The Brink transcript, you must run this script before doing any analysis.**

YouTube auto-captions contain overlapping caption window artifacts that cause every phrase to repeat 2-3 times per line. This script removes the duplicates, fixes garbled unicode characters, and reduces file size by ~60%. Analysing uncleaned transcripts will produce unreliable theme extraction.

### Usage
```
# Clean all transcripts (writes to /cleaned subfolder):
python3 ~/.openclaw/workspace-business/clean_transcripts.py

# Overwrite originals in place:
python3 ~/.openclaw/workspace-business/clean_transcripts.py --inplace

# Clean a single new file:
python3 ~/.openclaw/workspace-business/clean_transcripts.py --file intelligence/weekly/transcripts/onthebrink-XXXX.txt
```

Always run the cleaner before theme cataloging or delta analysis. Never analyse raw transcripts.
