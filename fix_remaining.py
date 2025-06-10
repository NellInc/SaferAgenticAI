#!/usr/bin/env python3

import re

def fix_remaining_tables():
    with open('framework.html', 'r') as f:
        content = f.read()
    
    print("Starting systematic fixes for remaining tables...")
    
    # Count starting unfixed tables
    start_count = content.count('N<br><br>N')
    print(f"Starting count: {start_count}")
    
    # Pattern 1: Simple 2 SFR tables - N,N pattern with exact matching stakeholders
    pattern_2sfr = r'<td>a\. ([^<]+?)<br><br>b\. ([^<]+?)</td>\s*<td>N<br><br>N</td>\s*<td>([^<]+?)<br><br>\3</td>\s*<td>([^<]+?)</td>'
    
    def replace_2sfr(match):
        sfr_a = match.group(1)
        sfr_b = match.group(2)
        stakeholder = match.group(3)
        evidence = match.group(4)
        
        return f"""<td>a. {sfr_a}</td>
                    <td class="sfr-align">N</td>
                    <td class="sfr-align">{stakeholder}</td>
                    <td rowspan="2">{evidence}</td>
                </tr>
                <tr>
                    <td>b. {sfr_b}</td>
                    <td class="sfr-align">N</td>
                    <td class="sfr-align">{stakeholder}</td>"""
    
    # Apply 2 SFR fixes
    content = re.sub(pattern_2sfr, replace_2sfr, content)
    
    # Pattern 2: Simple 3 SFR tables - N,N,N pattern
    pattern_3sfr = r'<td>a\. ([^<]+?)<br><br>b\. ([^<]+?)<br><br>c\. ([^<]+?)</td>\s*<td>N<br><br>N<br><br>N</td>\s*<td>([^<]+?)<br><br>\4<br><br>\4</td>\s*<td>([^<]+?)</td>'
    
    def replace_3sfr(match):
        sfr_a = match.group(1)
        sfr_b = match.group(2)
        sfr_c = match.group(3)
        stakeholder = match.group(4)
        evidence = match.group(5)
        
        return f"""<td>a. {sfr_a}</td>
                    <td class="sfr-align">N</td>
                    <td class="sfr-align">{stakeholder}</td>
                    <td rowspan="3">{evidence}</td>
                </tr>
                <tr>
                    <td>b. {sfr_b}</td>
                    <td class="sfr-align">N</td>
                    <td class="sfr-align">{stakeholder}</td>
                </tr>
                <tr>
                    <td>c. {sfr_c}</td>
                    <td class="sfr-align">N</td>
                    <td class="sfr-align">{stakeholder}</td>"""
    
    # Apply 3 SFR fixes
    content = re.sub(pattern_3sfr, replace_3sfr, content)
    
    # Pattern 3: Mixed N/I patterns for 3 SFRs - N,N,I
    pattern_3sfr_nni = r'<td>a\. ([^<]+?)<br><br>b\. ([^<]+?)<br><br>c\. ([^<]+?)</td>\s*<td>N<br><br>N<br><br>I</td>\s*<td>([^<]+?)<br><br>\4<br><br>\4</td>\s*<td>([^<]+?)</td>'
    
    def replace_3sfr_nni(match):
        sfr_a = match.group(1)
        sfr_b = match.group(2)
        sfr_c = match.group(3)
        stakeholder = match.group(4)
        evidence = match.group(5)
        
        return f"""<td>a. {sfr_a}</td>
                    <td class="sfr-align">N</td>
                    <td class="sfr-align">{stakeholder}</td>
                    <td rowspan="3">{evidence}</td>
                </tr>
                <tr>
                    <td>b. {sfr_b}</td>
                    <td class="sfr-align">N</td>
                    <td class="sfr-align">{stakeholder}</td>
                </tr>
                <tr>
                    <td>c. {sfr_c}</td>
                    <td class="sfr-align">I</td>
                    <td class="sfr-align">{stakeholder}</td>"""
    
    # Apply N,N,I fixes
    content = re.sub(pattern_3sfr_nni, replace_3sfr_nni, content)
    
    # Pattern 4: 4 SFR tables - N,N,N,N pattern
    pattern_4sfr = r'<td>a\. ([^<]+?)<br><br>b\. ([^<]+?)<br><br>c\. ([^<]+?)<br><br>d\. ([^<]+?)</td>\s*<td>N<br><br>N<br><br>N<br><br>N</td>\s*<td>([^<]+?)<br><br>\5<br><br>\5<br><br>\5</td>\s*<td>([^<]+?)</td>'
    
    def replace_4sfr(match):
        sfr_a = match.group(1)
        sfr_b = match.group(2)
        sfr_c = match.group(3)
        sfr_d = match.group(4)
        stakeholder = match.group(5)
        evidence = match.group(6)
        
        return f"""<td>a. {sfr_a}</td>
                    <td class="sfr-align">N</td>
                    <td class="sfr-align">{stakeholder}</td>
                    <td rowspan="4">{evidence}</td>
                </tr>
                <tr>
                    <td>b. {sfr_b}</td>
                    <td class="sfr-align">N</td>
                    <td class="sfr-align">{stakeholder}</td>
                </tr>
                <tr>
                    <td>c. {sfr_c}</td>
                    <td class="sfr-align">N</td>
                    <td class="sfr-align">{stakeholder}</td>
                </tr>
                <tr>
                    <td>d. {sfr_d}</td>
                    <td class="sfr-align">N</td>
                    <td class="sfr-align">{stakeholder}</td>"""
    
    # Apply 4 SFR fixes
    content = re.sub(pattern_4sfr, replace_4sfr, content)
    
    # Let me also try patterns that might have slightly different formatting
    
    # Pattern 5: Handle cases where stakeholders might not be identical (mixed stakeholder patterns)
    # This is common in many tables that might have D,I,O,M,U,R vs D,I,O,M,R patterns
    
    # Save the fixed content
    with open('framework.html', 'w') as f:
        f.write(content)
    
    # Count remaining unfixed tables
    end_count = content.count('N<br><br>N')
    fixed_count = start_count - end_count
    print(f"Fixed {fixed_count} tables")
    print(f"Remaining count: {end_count}")
    
    print("Done with systematic table fixes!")

if __name__ == "__main__":
    fix_remaining_tables() 