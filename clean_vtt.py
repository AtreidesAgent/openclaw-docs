#!/usr/bin/env python3
import argparse, re, os

def clean_vtt(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    content = re.sub(r'^WEBVTT.*?\n', '', content, flags=re.MULTILINE)
    content = re.sub(r'NOTE\s.*?\n\n', '', content, flags=re.DOTALL)
    content = re.sub(r'\d{2}:\d{2}:\d{2}\.\d{3}\s+-->\s+\d{2}:\d{2}:\d{2}\.\d{3}[^\n]*\n', '', content)
    content = re.sub(r'<[^>]+>', '', content)
    lines = content.split('\n')
    lines = [l.strip() for l in lines if l.strip() and not l.strip().isdigit()]
    fillers = {'[Music]', '[Applause]', '[Laughter]', 'Kind: captions', 'Language: en'}
    lines = [l for l in lines if l not in fillers]
    deduped, prev = [], None
    for line in lines:
        if line != prev:
            deduped.append(line)
            prev = line
    text = ' '.join(deduped)
    words = text.split()
    result = []
    i = 0
    while i < len(words):
        found_repeat = False
        for window in range(8, 3, -1):
            if i + window * 2 <= len(words):
                chunk = words[i:i+window]
                next_chunk = words[i+window:i+window*2]
                if chunk == next_chunk:
                    result.extend(chunk)
                    i += window * 2
                    found_repeat = True
                    break
        if not found_repeat:
            result.append(words[i])
            i += 1
    text = re.sub(r'\s+', ' ', ' '.join(result)).strip()
    if os.path.dirname(output_path):
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f'Cleaned: {len(text)} chars')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    clean_vtt(args.input, args.output)
