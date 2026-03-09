import re, argparse
from pathlib import Path

DEFAULT_INPUT  = Path("~/").expanduser() / ".openclaw/workspace-business/intelligence/weekly/transcripts"
DEFAULT_OUTPUT = Path("~/").expanduser() / ".openclaw/workspace-business/intelligence/weekly/transcripts/cleaned"

UNICODE_FIXES = [
    (r'u0002aj\b','Raj'),(r'u0002y\b','My'),(r'u0002rom\b','from'),
    (r'u0002om\b','from'),(r'u0002he\b','the'),(r'u0002hat\b','that'),
    (r'u0002his\b','this'),(r'u0002here\b','there'),(r'u0002hose\b','those'),
    (r'u0002hey\b','they'),(r'u0002o\b','to'),(r'u0002nd\b','and'),
    (r'u0002n\b','in'),(r'u0002t\b','it'),(r'u0002s\b','is'),
    (r'u0002ithout\b','without'),(r'u0002ith\b','with'),(r'u0002hich\b','which'),
    (r'u0002e\b','we'),(r'u0002',''),
]

def fix_unicode(text):
    for p,r in UNICODE_FIXES:
        text = re.sub(p,r,text)
    return text

def clean_interleaved(line):
    words = line.split()
    n = len(words)
    if n < 6:
        return line
    result = []
    i = 0
    changed = False
    while i < n:
        found = False
        for chunk_len in range((n-i)//2, 0, -1):
            chunk = words[i:i+chunk_len]
            nxt = i+chunk_len
            if nxt+chunk_len <= n and words[nxt:nxt+chunk_len] == chunk:
                result.extend(chunk)
                j = nxt
                while j+chunk_len <= n and words[j:j+chunk_len] == chunk:
                    j += chunk_len
                i = j
                found = True
                changed = True
                break
        if not found:
            result.append(words[i])
            i += 1
    return ' '.join(result) if changed else line

def shared_prefix_words(a, b):
    count = 0
    for x,y in zip(a.lower().split(), b.lower().split()):
        if x==y: count+=1
        else: break
    return count

def shared_suffix_words(a, b):
    count = 0
    for x,y in zip(reversed(a.lower().split()), reversed(b.lower().split())):
        if x==y: count+=1
        else: break
    return count

def remove_orphan_fragments(lines):
    result = []
    for i, line in enumerate(lines):
        s = line.strip()
        if not s:
            result.append(line)
            continue
        cw = len(s.split())
        frag = False
        if i+1 < len(lines):
            nx = lines[i+1].strip()
            sp = shared_prefix_words(s, nx)
            if cw < len(nx.split()) and sp >= 2 and sp/cw >= 0.4:
                frag = True
        if not frag and result:
            pv = result[-1].strip()
            if pv:
                ss = shared_suffix_words(s, pv)
                if cw < len(pv.split()) and ss >= 2 and ss/cw >= 0.4:
                    frag = True
        if not frag:
            result.append(line)
    return result

def clean_transcript(text):
    text = fix_unicode(text)
    lines = text.splitlines()
    cleaned = [clean_interleaved(l.strip()) for l in lines]
    cleaned = remove_orphan_fragments(cleaned)
    prev = None
    deduped = []
    for l in cleaned:
        if l != prev:
            deduped.append(l)
            prev = l
    text = '\n'.join(deduped)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip() + '\n'

def process_file(inp, out):
    raw = inp.read_text(encoding='utf-8', errors='replace')
    cleaned = clean_transcript(raw)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(cleaned, encoding='utf-8')
    o = len(raw.encode('utf-8'))
    c = len(cleaned.encode('utf-8'))
    print(f"  ✓ {inp.name:50s}  {o:>7,}B → {c:>7,}B  (-{100*(1-c/o):.0f}%)")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input',   type=Path, default=DEFAULT_INPUT)
    parser.add_argument('--output',  type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument('--file',    type=Path, default=None)
    parser.add_argument('--inplace', action='store_true')
    args = parser.parse_args()
    print('\n── On The Brink Transcript Cleaner ──────────────────────────────────')
    if args.file:
        src = args.file.expanduser().resolve()
        dst = src if args.inplace else args.output / src.name
        process_file(src, dst)
    else:
        src_dir = args.input.expanduser().resolve()
        txt_files = sorted(src_dir.glob('*.txt'))
        dst_dir = src_dir if args.inplace else args.output.expanduser().resolve()
        print(f'Input:  {src_dir}\nOutput: {dst_dir}\nFiles:  {len(txt_files)}\n')
        for f in txt_files:
            process_file(f, dst_dir / f.name)
    print('\n── Done ─────────────────────────────────────────────────────────────\n')

if __name__ == '__main__':
    main()
