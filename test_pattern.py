#!/usr/bin/env python3
import re

with open('framework.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Test different patterns to see what actually matches
patterns_to_test = [
    r'G\d+(?:\.\d+)*?\db\s–',
    r'G\d+\.?\d*b\s–',
    r'G\d+b\s–',
    r'G1b\s–',
    r'G1\.1b\s–'
]

for pattern in patterns_to_test:
    matches = re.findall(pattern, content)
    print(f"Pattern {pattern}: found {len(matches)} matches")
    if matches:
        print(f"  First match: {repr(matches[0])}")

# Let's also try manually building the pattern character by character
print("\nManual pattern test:")
# Look for 'G1b ' followed by en dash
manual_pattern = r'G1b\s\u2013'
matches = re.findall(manual_pattern, content)
print(f"Manual pattern G1b\\s\\u2013: found {len(matches)} matches")

# Try with raw string
print("\nRaw character test:")
en_dash = '\u2013'
space_en_pattern = f'G1b {en_dash}'
if space_en_pattern in content:
    print("Found 'G1b –' pattern in content!")
    # Count occurrences
    count = content.count(space_en_pattern)
    print(f"Count: {count}")
else:
    print("Pattern 'G1b –' NOT found in content")
    
# Check what we actually have
lines_with_g1b = [line for line in content.split('\n') if 'G1b' in line and '–' in line]
print(f"\nFound {len(lines_with_g1b)} lines with G1b and en dash")
if lines_with_g1b:
    print(f"First example: {repr(lines_with_g1b[0][:50])}") 