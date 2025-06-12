#!/usr/bin/env python3
import re

def analyze_characters():
    with open('framework.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find patterns that look like G#b or G#.#b followed by some character
    matches = re.findall(r'G\d+\.?\d*b\s*.\s*\w+', content)
    
    if matches:
        print('Found patterns:')
        for i, match in enumerate(matches[:5]):
            print(f'  {i+1}: {repr(match)}')
            # Show the character codes for non-ASCII characters
            for pos, char in enumerate(match):
                if ord(char) > 127:
                    print(f'    pos {pos}: {char} (U+{ord(char):04X})')
    else:
        print('No patterns found with current regex')
    
    # Also look specifically for lines with G#b
    lines_with_gb = [line for line in content.split('\n') if re.search(r'G\d+\.?\d*b', line)]
    
    print(f'\nFound {len(lines_with_gb)} lines with G#b pattern')
    if lines_with_gb:
        print('First few examples:')
        for line in lines_with_gb[:3]:
            print(f'  {line.strip()}')
            # Analyze the character after 'b'
            match = re.search(r'G\d+\.?\d*b(.)', line)
            if match:
                next_char = match.group(1)
                print(f'    Character after b: {repr(next_char)} (U+{ord(next_char):04X})')

if __name__ == "__main__":
    analyze_characters() 