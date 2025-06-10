import re

def fix_batch_3():
    with open('framework.html', 'r') as f:
        content = f.read()
    
    print("Starting batch 3 fixes...")
    
    # Fix G4.6b - Lack of Universality of Value Framework (4 SFRs)
    if 'Establish processes to identify situations where universal value frameworks require contextual adaptation' in content:
        content = re.sub(
            r'(<td>a\. Establish processes to identify situations where universal value frameworks require contextual adaptation\.)<br><br>(b\. Develop structured approaches for appropriate value framework modification across different deployment contexts\.)<br><br>(c\. Implement monitoring systems to detect and respond to value framework misalignments\.)<br><br>(d\. Create fallback protocols for situations where value frameworks prove inadequate\.)</td>\s*<td>N<br><br>N<br><br>N<br><br>I</td>',
            r'\1</td>\n                    <td class="sfr-align">N</td>\n                    <td class="sfr-align">D, I, O, M, R</td>\n                    <td rowspan="4">I. Detailed intervention and fallback plans for addressing value framework failures or deviations.<br><br>II. Implementation plans for value framework refinement, including: Contextual adaptation procedures, testing methodologies, and validation processes.</td>\n                </tr>\n                <tr>\n                    <td>\2</td>\n                    <td class="sfr-align">N</td>\n                    <td class="sfr-align">D, I, O, M, R</td>\n                </tr>\n                <tr>\n                    <td>\3</td>\n                    <td class="sfr-align">N</td>\n                    <td class="sfr-align">D, I, O, M, R</td>\n                </tr>\n                <tr>\n                    <td>\4</td>\n                    <td class="sfr-align">I</td>\n                    <td class="sfr-align">D, I, O, M, R</td>',
            content
        )
        print("Fixed G4.6b")
    
    # Fix G4.7b - Conflictual Contextual Values (4 SFRs)
    if 'Implement processes to identify differing value positions across agents and contexts' in content:
        content = re.sub(
            r'(<td>a\. Implement processes to identify differing value positions across agents and contexts\.)<br><br>(b\. Develop mechanisms to detect potential conflicts between user values and operational context requirements\.)<br><br>(c\. Establish protocols for value conflict resolution through negotiation or controlled disengagement\.)<br><br>(d\. Maintain comprehensive records of value modifications and adaptations across different contexts\.)</td>\s*<td>N<br><br>N<br><br>N<br><br>I</td>',
            r'\1</td>\n                    <td class="sfr-align">N</td>\n                    <td class="sfr-align">D, I, O, M, R</td>\n                    <td rowspan="4">I. Technical documentation demonstrating: Value conflict detection capabilities, resolution mechanism implementations, and disengagement protocols.<br><br>II. System logs recording: Identified value conflicts, negotiation processes, resolution outcomes, and modified value implementations.</td>\n                </tr>\n                <tr>\n                    <td>\2</td>\n                    <td class="sfr-align">N</td>\n                    <td class="sfr-align">D, I, O, M, R</td>\n                </tr>\n                <tr>\n                    <td>\3</td>\n                    <td class="sfr-align">N</td>\n                    <td class="sfr-align">D, I, O, M, R</td>\n                </tr>\n                <tr>\n                    <td>\4</td>\n                    <td class="sfr-align">I</td>\n                    <td class="sfr-align">D, I, O, M, R</td>',
            content
        )
        print("Fixed G4.7b")
    
    # Fix G4.8b - Challenges in Encoding of Relevant Value Systems (4 SFRs)
    if 'Develop robust methods for encoding values that work across varied operational contexts' in content:
        content = re.sub(
            r'(<td>a\. Develop robust methods for encoding values that work across varied operational contexts\.)<br><br>(b\. Implement safeguards for handling situations beyond the system\'s encoded value parameters\.)<br><br>(c\. Establish protocols for identifying and managing out-of-distribution value scenarios\.)<br><br>(d\. Maintain alignment capabilities during complex planning operations\.)</td>\s*<td>N<br><br>I<br><br>N<br><br>I</td>',
            r'\1</td>\n                    <td class="sfr-align">N</td>\n                    <td class="sfr-align">D, I, O, M, R</td>\n                    <td rowspan="4">I. Documentation of safeguard processes for scenarios where: A value codex proves insufficient, external factors exceed system parameters, or operational environments fall outside encoded boundaries.<br><br>II. Detailed mapping of objectives and decision parameters for anticipated complex environments. Framework documentation for handling unexpected scenarios, including: Detection methods, response protocols, and alignment maintenance procedures.</td>\n                </tr>\n                <tr>\n                    <td>\2</td>\n                    <td class="sfr-align">I</td>\n                    <td class="sfr-align">D, I, O, M, R</td>\n                </tr>\n                <tr>\n                    <td>\3</td>\n                    <td class="sfr-align">N</td>\n                    <td class="sfr-align">D, I, O, M, R</td>\n                </tr>\n                <tr>\n                    <td>\4</td>\n                    <td class="sfr-align">I</td>\n                    <td class="sfr-align">D, I, O, M, R</td>',
            content
        )
        print("Fixed G4.8b")
    
    # Fix G5.2 - Clarity of Human Expectations (4 SFRs)
    if 'Capture and document human expectations accurately in system requirements specifications' in content:
        content = re.sub(
            r'(<td>a\. Capture and document human expectations accurately in system requirements specifications\.)<br><br>(b\. Maintain clear, accessible documentation of expected AAI behaviors and outputs\.)<br><br>(c\. Implement feedback mechanisms for stakeholders to express their expectations and experiences\.)<br><br>(d\. Establish and maintain traceable links between documented expectations and actual system behaviors\.)</td>\s*<td>N<br><br>N<br><br>I<br><br>N</td>',
            r'\1</td>\n                    <td class="sfr-align">N</td>\n                    <td class="sfr-align">D, I, O, M, R</td>\n                    <td rowspan="4">I. Core system documentation including requirements specifications detailing human expectations, design specifications for expectation handling, and validation records demonstrating alignment between requirements and implementation.<br><br>II. User-focused documentation including comprehensive behavior specifications, regular system updates, and feedback logs showing ongoing expectation alignment between users and system performance.<br><br>III. Verification documentation including function-expectation mapping records, comparative audit reports of expected versus actual behaviors, and thorough records of any expectation-behavior discrepancies with their resolutions.</td>\n                </tr>\n                <tr>\n                    <td>\2</td>\n                    <td class="sfr-align">N</td>\n                    <td class="sfr-align">D, I, O, M, R</td>\n                </tr>\n                <tr>\n                    <td>\3</td>\n                    <td class="sfr-align">I</td>\n                    <td class="sfr-align">D, I, O, M, R</td>\n                </tr>\n                <tr>\n                    <td>\4</td>\n                    <td class="sfr-align">N</td>\n                    <td class="sfr-align">D, I, O, M, R</td>',
            content
        )
        print("Fixed G5.2")
    
    # Fix G5.3 - Prioritization of Human User Expectations (3 SFRs)
    if 'Ensure human user expectations take priority over other considerations in system design' in content:
        content = re.sub(
            r'(<td>a\. Ensure human user expectations take priority over other considerations in system design and operation\.)<br><br>(b\. Implement transparency metrics directly linked to stakeholder values and expectations\.)<br><br>(c\. Maintain adaptable transparency measures that evolve with user needs and feedback\.)</td>\s*<td>N<br><br>I<br><br>I</td>',
            r'\1</td>\n                    <td class="sfr-align">N</td>\n                    <td class="sfr-align">D, I, O, M, R</td>\n                    <td rowspan="3">I. System design documentation including requirements specifications demonstrating prioritization of human expectations, transparency metrics aligned with user values, and complete process documentation for implementing adaptations.<br><br>II. User feedback evidence including stakeholder survey results, analysis reports linking transparency to satisfaction metrics, and case studies demonstrating improved outcomes through adaptive transparency.<br><br>III. System adaptation records including detailed change logs of transparency measure adjustments, failure analysis reports, and documentation of mitigation efforts when user expectations are not met.</td>\n                </tr>\n                <tr>\n                    <td>\2</td>\n                    <td class="sfr-align">I</td>\n                    <td class="sfr-align">D, I, O, M, R</td>\n                </tr>\n                <tr>\n                    <td>\3</td>\n                    <td class="sfr-align">I</td>\n                    <td class="sfr-align">D, I, O, M, R</td>',
            content
        )
        print("Fixed G5.3")
    
    with open('framework.html', 'w') as f:
        f.write(content)
    
    print("Done with batch 3!")

if __name__ == "__main__":
    fix_batch_3() 