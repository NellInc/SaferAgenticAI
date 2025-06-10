#!/usr/bin/env python3

import re

def fix_advanced_patterns():
    with open('framework.html', 'r') as f:
        content = f.read()
    
    print("Starting advanced pattern fixes...")
    start_count = content.count('N<br><br>N')
    print(f"Starting count: {start_count}")
    
    # Pattern 1: Handle 3 SFR tables with indented formatting (like G6.3b, G6.4b)
    # Look for tables with indented structure
    indented_3sfr_pattern = r'<td>\s*a\.\s*([^<]+?)<br><br>\s*b\.\s*([^<]+?)<br><br>\s*c\.\s*([^<]+?)\s*</td>\s*<td>N<br><br>N<br><br>N</td>\s*<td>([^<]+?)<br><br>\4<br><br>\4</td>\s*<td>\s*([^<]+?)\s*</td>'
    
    def replace_indented_3sfr(match):
        sfr_a = match.group(1).strip()
        sfr_b = match.group(2).strip()
        sfr_c = match.group(3).strip()
        stakeholder = match.group(4)
        evidence = match.group(5).strip()
        
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
    
    content = re.sub(indented_3sfr_pattern, replace_indented_3sfr, content, flags=re.DOTALL)
    
    # Pattern 2: Handle 2 SFR tables with different stakeholder patterns
    # Be careful to preserve exact stakeholder text to avoid width issues
    pattern_2sfr_flexible = r'<td>a\.\s*([^<]+?)<br><br>b\.\s*([^<]+?)</td>\s*<td>N<br><br>N</td>\s*<td>([^<]+?)<br><br>([^<]+?)</td>\s*<td>([^<]+?)</td>'
    
    def replace_2sfr_flexible(match):
        sfr_a = match.group(1).strip()
        sfr_b = match.group(2).strip()
        stakeholder_a = match.group(3).strip()
        stakeholder_b = match.group(4).strip()
        evidence = match.group(5)
        
        # Check if stakeholders are the same (to avoid breaking tables with intentionally different stakeholders)
        if stakeholder_a == stakeholder_b:
            return f"""<td>a. {sfr_a}</td>
                    <td class="sfr-align">N</td>
                    <td class="sfr-align">{stakeholder_a}</td>
                    <td rowspan="2">{evidence}</td>
                </tr>
                <tr>
                    <td>b. {sfr_b}</td>
                    <td class="sfr-align">N</td>
                    <td class="sfr-align">{stakeholder_b}</td>"""
        else:
            # Return original if stakeholders differ (preserve alternating pattern)
            return match.group(0)
    
    content = re.sub(pattern_2sfr_flexible, replace_2sfr_flexible, content)
    
    # Pattern 3: Mixed I patterns for 4 SFR tables
    pattern_4sfr_iiii = r'<td>a\.\s*([^<]+?)<br><br>b\.\s*([^<]+?)<br><br>c\.\s*([^<]+?)<br><br>d\.\s*([^<]+?)</td>\s*<td>I<br><br>I<br><br>I<br><br>I</td>\s*<td>([^<]+?)<br><br>\5<br><br>\5<br><br>\5</td>\s*<td>([^<]+?)</td>'
    
    def replace_4sfr_iiii(match):
        sfr_a = match.group(1).strip()
        sfr_b = match.group(2).strip()
        sfr_c = match.group(3).strip()
        sfr_d = match.group(4).strip()
        stakeholder = match.group(5)
        evidence = match.group(6)
        
        return f"""<td>a. {sfr_a}</td>
                    <td class="sfr-align">I</td>
                    <td class="sfr-align">{stakeholder}</td>
                    <td rowspan="4">{evidence}</td>
                </tr>
                <tr>
                    <td>b. {sfr_b}</td>
                    <td class="sfr-align">I</td>
                    <td class="sfr-align">{stakeholder}</td>
                </tr>
                <tr>
                    <td>c. {sfr_c}</td>
                    <td class="sfr-align">I</td>
                    <td class="sfr-align">{stakeholder}</td>
                </tr>
                <tr>
                    <td>d. {sfr_d}</td>
                    <td class="sfr-align">I</td>
                    <td class="sfr-align">{stakeholder}</td>"""
    
    content = re.sub(pattern_4sfr_iiii, replace_4sfr_iiii, content)
    
    # Pattern 4: Handle specific mixed N/I patterns - 3 SFR with N,I,N
    pattern_3sfr_nin = r'<td>a\.\s*([^<]+?)<br><br>b\.\s*([^<]+?)<br><br>c\.\s*([^<]+?)</td>\s*<td>N<br><br>I<br><br>N</td>\s*<td>([^<]+?)<br><br>\4<br><br>\4</td>\s*<td>([^<]+?)</td>'
    
    def replace_3sfr_nin(match):
        sfr_a = match.group(1).strip()
        sfr_b = match.group(2).strip()
        sfr_c = match.group(3).strip()
        stakeholder = match.group(4)
        evidence = match.group(5)
        
        return f"""<td>a. {sfr_a}</td>
                    <td class="sfr-align">N</td>
                    <td class="sfr-align">{stakeholder}</td>
                    <td rowspan="3">{evidence}</td>
                </tr>
                <tr>
                    <td>b. {sfr_b}</td>
                    <td class="sfr-align">I</td>
                    <td class="sfr-align">{stakeholder}</td>
                </tr>
                <tr>
                    <td>c. {sfr_c}</td>
                    <td class="sfr-align">N</td>
                    <td class="sfr-align">{stakeholder}</td>"""
    
    content = re.sub(pattern_3sfr_nin, replace_3sfr_nin, content)
    
    # Save the fixed content
    with open('framework.html', 'w') as f:
        f.write(content)
    
    end_count = content.count('N<br><br>N')
    fixed_count = start_count - end_count
    print(f"Fixed {fixed_count} tables")
    print(f"Remaining count: {end_count}")
    
    print("Done with advanced pattern fixes!")

if __name__ == "__main__":
    fix_advanced_patterns() 