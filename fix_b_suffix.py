#!/usr/bin/env python3
import re

def convert_b_suffix_to_underlined(text):
    """Convert 'b' suffix patterns to underlined numbers.
    
    Examples:
    G1b -> G1̲
    G1.1b -> G1.1̲ 
    G1b.1b -> G1̲.1̲
    """
    # Pattern that captures the complete number sequence ending with a digit before 'b'
    pattern = r'G(\d+(?:\.\d+)*)b(\s–)'
    
    def replace_match(match):
        full_number = match.group(1)  # Complete number sequence (e.g., "1" or "1.1")
        suffix = match.group(2)  # What comes after 'b' (space + en dash)
        
        # Get the last digit and replace it with underlined version
        last_digit = full_number[-1]
        prefix = full_number[:-1]  # Everything except the last digit
        underlined_digit = last_digit + '\u0332'
        
        return f"G{prefix}{underlined_digit}{suffix}"
    
    return re.sub(pattern, replace_match, text)

def test_pattern():
    """Test the pattern with some examples"""
    test_cases = [
        "G1b – Test",
        "G1.1b – Test", 
        "G1b.1b – Test",
        "<h3>G1.1b – System Incorrigibility and Resistance to Change</h3>",
        "'Inhibitor G1b – Opaque Agency Capabilities & Advances',"
    ]
    
    # First test if the regex finds the patterns
    for test in test_cases:
        match = re.search(r'G(\d+(?:\.\d+)*)b(\s–)', test)
        if match:
            print(f"Found match in '{test}': groups = {match.groups()}")
        else:
            print(f"No match in '{test}'")
    
    print("\nTesting conversion:")
    for test in test_cases:
        result = convert_b_suffix_to_underlined(test)
        print(f"'{test}' -> '{result}'")
        if test != result:
            print("  *** CHANGED ***")

def main():
    # First test the pattern
    print("Testing regex pattern:")
    test_pattern()
    print()
    
    # Read the framework.html file
    with open('framework.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Count matches before conversion using our pattern
    original_matches = len(re.findall(r'G\d+(?:\.\d+)*b\s–', content))
    print(f"Found {original_matches} patterns to convert")
    
    # Apply the conversion
    converted_content = convert_b_suffix_to_underlined(content)
    
    # Count matches after conversion to verify
    remaining_matches = len(re.findall(r'G\d+(?:\.\d+)*b\s–', converted_content))
    print(f"Remaining unconverted patterns: {remaining_matches}")
    
    # Show a sample of converted text
    sample_match = re.search(r'G\d+(?:\.\d+)*\u0332\s–', converted_content)
    if sample_match:
        print(f"Sample converted text: {repr(sample_match.group(0))}")
    
    # Write the result back
    with open('framework.html', 'w', encoding='utf-8') as f:
        f.write(converted_content)
    
    print("Successfully converted all 'b' suffixes to underlined numbers in framework.html")

if __name__ == "__main__":
    main() 