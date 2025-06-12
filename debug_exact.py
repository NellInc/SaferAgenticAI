#!/usr/bin/env python3
import re

with open('framework.html', 'r') as f:
    content = f.read()

# Find a specific pattern and show the characters around 'b'
match = re.search(r'G1\.1b.{10}', content)
if match:
    text = match.group(0)
    print('Found text:', repr(text))
    for i, char in enumerate(text):
        print(f'{i}: {char} (U+{ord(char):04X})')
        
print()

# Also check what comes immediately after all 'b' patterns
matches = re.findall(r'G\d+(?:\.\d+)*?b(.{5})', content)
print(f'Found {len(matches)} patterns, first few after "b":')
for i, after_b in enumerate(matches[:5]):
    print(f'{i+1}: {repr(after_b)}')
    for j, char in enumerate(after_b):
        if j < 2:  # Just first 2 chars
            print(f'  {j}: {char} (U+{ord(char):04X})') 