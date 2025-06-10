import re

def fix_final_batch():
    with open('framework.html', 'r') as f:
        content = f.read()
    
    print("Starting final batch fixes...")
    
    # G5.4 - Interpretability and Traceability of Reasoning (3 SFRs)
    if 'Implement systems that can generate clear, accurate and accessible explanations for all reasoning chains' in content:
        content = re.sub(
            r'(<td>a\. Implement systems that can generate clear, accurate and accessible explanations for all reasoning chains and decision processes\.)<br><br>(b\. Establish documentation requirements for reasoning preconditions, assumptions, and logical steps\.)<br><br>(c\. Maintain transparency mechanisms that remain interpretable across different stakeholder groups and technical expertise levels\.)</td>\s*<td>N<br><br>N<br><br>N</td>',
            r'\1</td>\n                    <td class="sfr-align">N</td>\n                    <td class="sfr-align">D, I, O, M, R</td>\n                    <td rowspan="3">I. Evidence of comprehensive explanation systems covering all reasoning chains and decision processes.<br><br>II. Documentation demonstrating clear reasoning preconditions, assumptions, and logical steps.<br><br>III. Stakeholder feedback demonstrating successful interpretation of transparency mechanisms across different technical expertise levels.</td>\n                </tr>\n                <tr>\n                    <td>\2</td>\n                    <td class="sfr-align">N</td>\n                    <td class="sfr-align">D, I, O, M, R</td>\n                </tr>\n                <tr>\n                    <td>\3</td>\n                    <td class="sfr-align">N</td>\n                    <td class="sfr-align">D, I, O, M, R</td>',
            content
        )
        print("Fixed G5.4")
    
    # G5.1b - Objective Targeting (3 SFRs)
    if 'Implement systems that clearly define and document all operational objectives' in content:
        content = re.sub(
            r'(<td>a\. Implement systems that clearly define and document all operational objectives and their relationships to broader system goals\.)<br><br>(b\. Maintain transparent tracking of objective changes, modifications, and evolutions throughout system operation\.)<br><br>(c\. Establish clear validation processes to ensure objectives remain aligned with intended system purpose\.)</td>\s*<td>N<br><br>N<br><br>I</td>',
            r'\1</td>\n                    <td class="sfr-align">N</td>\n                    <td class="sfr-align">D, I, O, M, R</td>\n                    <td rowspan="3">I. Comprehensive documentation of all operational objectives including their hierarchical relationships and connections to broader system goals.<br><br>II. Complete audit trails showing objective modifications, rationale for changes, and impact assessments.<br><br>III. Regular validation reports demonstrating objective-purpose alignment with corrective actions for misalignments.</td>\n                </tr>\n                <tr>\n                    <td>\2</td>\n                    <td class="sfr-align">N</td>\n                    <td class="sfr-align">D, I, O, M, R</td>\n                </tr>\n                <tr>\n                    <td>\3</td>\n                    <td class="sfr-align">I</td>\n                    <td class="sfr-align">D, I, O, M, R</td>',
            content
        )
        print("Fixed G5.1b")
    
    # Look for patterns we can fix automatically using simple text replacement
    
    # Pattern 1: Simple 2 SFR tables with N, N pattern
    two_sfr_pattern = r'(<td>a\. [^<]+?)<br><br>(b\. [^<]+?)</td>\s*<td>N<br><br>N</td>\s*<td>([^<]+?)<br><br>\3</td>\s*<td>([^<]+?)</td>'
    
    def replace_two_sfr(match):
        sfr_a = match.group(1)
        sfr_b = match.group(2)
        stakeholder = match.group(3)
        evidence = match.group(4)
        
        return f"""{sfr_a}</td>
                    <td class="sfr-align">N</td>
                    <td class="sfr-align">{stakeholder}</td>
                    <td rowspan="2">{evidence}</td>
                </tr>
                <tr>
                    <td>{sfr_b}</td>
                    <td class="sfr-align">N</td>
                    <td class="sfr-align">{stakeholder}</td>
                </tr>"""
    
    # Apply the two SFR pattern fix
    content = re.sub(two_sfr_pattern, replace_two_sfr, content)
    
    # Pattern 2: Simple 3 SFR tables with N, N, N pattern
    three_sfr_pattern = r'(<td>a\. [^<]+?)<br><br>(b\. [^<]+?)<br><br>(c\. [^<]+?)</td>\s*<td>N<br><br>N<br><br>N</td>\s*<td>([^<]+?)<br><br>\4<br><br>\4</td>\s*<td>([^<]+?)</td>'
    
    def replace_three_sfr(match):
        sfr_a = match.group(1)
        sfr_b = match.group(2)
        sfr_c = match.group(3)
        stakeholder = match.group(4)
        evidence = match.group(5)
        
        return f"""{sfr_a}</td>
                    <td class="sfr-align">N</td>
                    <td class="sfr-align">{stakeholder}</td>
                    <td rowspan="3">{evidence}</td>
                </tr>
                <tr>
                    <td>{sfr_b}</td>
                    <td class="sfr-align">N</td>
                    <td class="sfr-align">{stakeholder}</td>
                </tr>
                <tr>
                    <td>{sfr_c}</td>
                    <td class="sfr-align">N</td>
                    <td class="sfr-align">{stakeholder}</td>
                </tr>"""
    
    # Apply the three SFR pattern fix
    content = re.sub(three_sfr_pattern, replace_three_sfr, content)
    
    # Let me add some manual fixes for tables I can see in the grep output
    
    # G6.1 - 4 SFRs table
    if 'Implement comprehensive human oversight mechanisms throughout the AI system lifecycle' in content:
        content = re.sub(
            r'(<td>a\. Implement comprehensive human oversight mechanisms throughout the AI system lifecycle\.)<br><br>(b\. Establish clear authority structures and decision-making protocols between human operators and AI systems\.)<br><br>(c\. Maintain human oversight capabilities that can effectively intervene in AI decision-making processes\.)<br><br>(d\. Ensure human oversight remains meaningful and effective as AI capabilities advance\.)</td>\s*<td>N<br><br>N<br><br>N<br><br>N</td>',
            r'\1</td>\n                    <td class="sfr-align">N</td>\n                    <td class="sfr-align">D, I, O, M, R</td>\n                    <td rowspan="4">I. Documentation of oversight protocols and procedures covering the entire AI system lifecycle.<br><br>II. Evidence of clear authority structures and decision-making protocols between human operators and AI systems.<br><br>III. Records demonstrating effective human intervention capabilities in AI decision-making processes.<br><br>IV. Assessment reports showing maintained oversight effectiveness as AI capabilities advance.</td>\n                </tr>\n                <tr>\n                    <td>\2</td>\n                    <td class="sfr-align">N</td>\n                    <td class="sfr-align">D, I, O, M, R</td>\n                </tr>\n                <tr>\n                    <td>\3</td>\n                    <td class="sfr-align">N</td>\n                    <td class="sfr-align">D, I, O, M, R</td>\n                </tr>\n                <tr>\n                    <td>\4</td>\n                    <td class="sfr-align">N</td>\n                    <td class="sfr-align">D, I, O, M, R</td>',
            content
        )
        print("Fixed G6.1")
    
    with open('framework.html', 'w') as f:
        f.write(content)
    
    print("Done with final batch!")

if __name__ == "__main__":
    fix_final_batch() 