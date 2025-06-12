#!/usr/bin/env python3
import re
import glob

def convert_all_b_patterns(text):
    """Convert all 'b' suffix patterns to underlined numbers in various contexts."""
    
    # Function to create underlined version of the last digit in a number sequence
    def underline_last_digit(number_sequence):
        if not number_sequence:
            return number_sequence
        last_digit = number_sequence[-1]
        prefix = number_sequence[:-1]
        underlined_digit = last_digit + '\u0332'
        return prefix + underlined_digit
    
    # Pattern 1: G#b.# (like G1b.1, G2b.3, etc.)
    def replace_gb_dot_pattern(match):
        number_before_b = match.group(1)
        number_after_dot = match.group(2)
        suffix = match.group(3)
        
        underlined_before_b = underline_last_digit(number_before_b)
        return f"G{underlined_before_b}.{number_after_dot}{suffix}"
    
    text = re.sub(r'G(\d+(?:\.\d+)*)b\.(\d+)(\s|$|–|\s–|</|>|\)|\,|"|/)', replace_gb_dot_pattern, text)
    
    # Pattern 2: G#b.#b (like G1b.1b, G2b.2b, etc.)
    def replace_gb_dot_gb_pattern(match):
        number_before_first_b = match.group(1)
        number_between = match.group(2)
        suffix = match.group(3)
        
        underlined_before_first_b = underline_last_digit(number_before_first_b)
        underlined_after_dot = underline_last_digit(number_between)
        return f"G{underlined_before_first_b}.{underlined_after_dot}{suffix}"
    
    text = re.sub(r'G(\d+(?:\.\d+)*)b\.(\d+)b(\s|$|–|\s–|</|>|\)|\,|"|/)', replace_gb_dot_gb_pattern, text)
    
    # Pattern 3: Remaining G#b patterns in various contexts (not followed by dot)
    def replace_remaining_gb_pattern(match):
        number_sequence = match.group(1)
        suffix = match.group(2)
        
        underlined_sequence = underline_last_digit(number_sequence)
        return f"G{underlined_sequence}{suffix}"
    
    text = re.sub(r'G(\d+(?:\.\d+)*)b(\s|$|–|\s–|</|>|\)|\,|"|_|\-|/)', replace_remaining_gb_pattern, text)
    
    return text

def analyze_file_patterns(filename):
    """Analyze what patterns are in a specific file."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return 0
    
    # Find all G#b patterns
    all_gb_patterns = re.findall(r'G\d+(?:\.\d+)*b(?:\.\d+b?)?', content)
    
    if all_gb_patterns:
        print(f"{filename}: Found {len(all_gb_patterns)} G#b patterns")
        # Show a few examples
        examples = list(set(all_gb_patterns))[:5]  # Remove duplicates and show first 5
        print(f"  Examples: {examples}")
    
    return len(all_gb_patterns)

def process_file(filename):
    """Process a single file to convert b patterns."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Count patterns before conversion
        original_patterns = len(re.findall(r'G\d+(?:\.\d+)*b', content))
        
        if original_patterns == 0:
            return 0, 0
        
        # Apply conversions
        converted_content = convert_all_b_patterns(content)
        
        # Count patterns after conversion
        remaining_patterns = len(re.findall(r'G\d+(?:\.\d+)*b', converted_content))
        
        # Write back to file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(converted_content)
        
        converted_count = original_patterns - remaining_patterns
        print(f"{filename}: Converted {converted_count} patterns, {remaining_patterns} remaining")
        
        return converted_count, remaining_patterns
        
    except Exception as e:
        print(f"Error processing {filename}: {e}")
        return 0, 0

def main():
    # Find all HTML files to process
    html_files = glob.glob('*.html')
    print(f"Found {len(html_files)} HTML files to check")
    
    print("\n=== ANALYZING PATTERNS IN ALL FILES ===")
    total_patterns = 0
    for filename in html_files:
        pattern_count = analyze_file_patterns(filename)
        total_patterns += pattern_count
    
    print(f"\nTotal G#b patterns across all files: {total_patterns}")
    
    if total_patterns == 0:
        print("No patterns found to convert!")
        return
    
    print("\n=== CONVERTING PATTERNS ===")
    total_converted = 0
    total_remaining = 0
    
    for filename in html_files:
        converted, remaining = process_file(filename)
        total_converted += converted
        total_remaining += remaining
    
    print(f"\n=== SUMMARY ===")
    print(f"Total patterns converted: {total_converted}")
    print(f"Total patterns remaining: {total_remaining}")
    print("Successfully processed all HTML files!")

if __name__ == "__main__":
    main() 