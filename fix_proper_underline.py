#!/usr/bin/env python3
import re
import glob

def convert_combining_to_css_underline(text):
    """Convert Unicode combining underline characters to CSS-based underlines with span elements."""
    
    def replace_underlined_digit(match):
        # Extract the digit with combining underline
        underlined_char = match.group(0)
        # Remove the combining underline character (U+0332)
        clean_digit = underlined_char.replace('\u0332', '')
        # Wrap in span with CSS class for underline
        return f'<span class="underlined-digit">{clean_digit}</span>'
    
    # Pattern to match any digit followed by combining underline character
    pattern = r'\d\u0332'
    
    return re.sub(pattern, replace_underlined_digit, text)

def add_css_styles():
    """Add CSS styles for the underlined digits to psychopathia-styles.css"""
    css_addition = """
/* Proper underline styling for inhibitor framework numbers */
.underlined-digit {
    text-decoration: underline;
    text-decoration-thickness: 1.5px;
    text-underline-offset: 2px;
    text-decoration-color: currentColor;
    font-family: inherit;
    font-weight: inherit;
    font-size: inherit;
}

/* Ensure underline looks good in headings */
h1 .underlined-digit,
h2 .underlined-digit, 
h3 .underlined-digit {
    text-decoration-thickness: 2px;
    text-underline-offset: 3px;
}

/* Navigation underline styling */
.nav-container .underlined-digit {
    text-decoration-thickness: 1px;
    text-underline-offset: 1px;
}
"""
    
    with open('psychopathia-styles.css', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add the CSS if it's not already there
    if '.underlined-digit' not in content:
        content += css_addition
        
        with open('psychopathia-styles.css', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("Added CSS styles for proper underlines")
    else:
        print("CSS styles already present")

def process_file(filename):
    """Process a single HTML file to convert combining underlines to CSS underlines."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Count patterns before conversion
        original_patterns = len(re.findall(r'\d\u0332', content))
        
        if original_patterns == 0:
            return 0
        
        # Apply conversions
        converted_content = convert_combining_to_css_underline(content)
        
        # Count patterns after conversion to verify
        remaining_patterns = len(re.findall(r'\d\u0332', converted_content))
        
        # Write back to file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(converted_content)
        
        converted_count = original_patterns - remaining_patterns
        print(f"{filename}: Converted {converted_count} combining underlines to CSS underlines")
        
        return converted_count
        
    except Exception as e:
        print(f"Error processing {filename}: {e}")
        return 0

def update_navbar_js():
    """Update navbar.js to create span elements instead of combining characters."""
    
    new_function = '''    // Function to convert 'b' suffix to CSS underlined number
    function convertBSuffixToUnderlined(text) {
        // Pattern matches: G<num>b or G<num>.<num>b followed by space and en dash
        return text.replace(/G(\\d+(?:\\.\\d+)*)b(\\s|$|–)/g, (match, fullNumber, suffix) => {
            const lastDigit = fullNumber.slice(-1);
            const prefix = fullNumber.slice(0, -1);
            const underlinedDigit = `<span class="underlined-digit">${lastDigit}</span>`;
            return `G${prefix}${underlinedDigit}${suffix}`;
        });
    }'''
    
    try:
        with open('assets/scripts/navbar.js', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and replace the existing function
        pattern = r'    // Function to convert \'b\' suffix to underlined number.*?return.*?}\);.*?    }'
        
        if re.search(pattern, content, re.DOTALL):
            updated_content = re.sub(pattern, new_function, content, flags=re.DOTALL)
            
            with open('assets/scripts/navbar.js', 'w', encoding='utf-8') as f:
                f.write(updated_content)
            
            print("Updated navbar.js to use CSS underlines")
        else:
            print("Could not find the function to replace in navbar.js")
            
    except Exception as e:
        print(f"Error updating navbar.js: {e}")

def main():
    print("=== CONVERTING COMBINING UNDERLINES TO CSS UNDERLINES ===")
    
    # Add CSS styles first
    add_css_styles()
    
    # Update navbar.js
    update_navbar_js()
    
    # Find all HTML files to process
    html_files = glob.glob('*.html')
    print(f"Found {len(html_files)} HTML files to process")
    
    total_converted = 0
    
    for filename in html_files:
        converted = process_file(filename)
        total_converted += converted
    
    print(f"\n=== SUMMARY ===")
    print(f"Total combining underlines converted to CSS underlines: {total_converted}")
    print("Framework numbers now use proper CSS underlines instead of Unicode combining characters!")

if __name__ == "__main__":
    main() 