#!/usr/bin/env python3
import re

def convert_id_b_patterns(text):
    """Convert 'b' suffix patterns in HTML id attributes."""
    
    def replace_id_pattern(match):
        full_id = match.group(1)  # The complete id content
        
        # Convert any g#b patterns within the id (note: ids use lowercase 'g')
        def replace_gb_in_id(gb_match):
            number = gb_match.group(1)  # The number before 'b'
            last_digit = number[-1]
            prefix = number[:-1]
            underlined_digit = last_digit + '\u0332'
            return f'g{prefix}{underlined_digit}'
        
        converted_id = re.sub(r'g(\d+)b\b', replace_gb_in_id, full_id)
        
        return f'id="{converted_id}"'
    
    # Pattern to match id attributes containing g#b patterns
    text = re.sub(r'id="([^"]*g\d+b[^"]*)"', replace_id_pattern, text)
    
    return text

def main():
    with open('framework.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find remaining patterns in id attributes
    id_patterns = re.findall(r'id="[^"]*g\d+b[^"]*"', content)
    print(f"Found {len(id_patterns)} id attributes with g#b patterns:")
    for pattern in id_patterns:
        print(f"  {pattern}")
    
    if not id_patterns:
        print("No id patterns found to convert!")
        return
    
    # Convert the patterns
    converted_content = convert_id_b_patterns(content)
    
    # Check what changed
    new_id_patterns = re.findall(r'id="[^"]*g\d+\u0332[^"]*"', converted_content)
    print(f"\nAfter conversion, found {len(new_id_patterns)} id attributes with underlined patterns:")
    for pattern in new_id_patterns:
        print(f"  {pattern}")
    
    # Check for any remaining unconverted patterns
    remaining_patterns = re.findall(r'id="[^"]*g\d+b[^"]*"', converted_content)
    print(f"Remaining unconverted patterns: {len(remaining_patterns)}")
    
    # Write back
    with open('framework.html', 'w', encoding='utf-8') as f:
        f.write(converted_content)
    
    print("Successfully converted id attribute patterns!")

if __name__ == "__main__":
    main() 