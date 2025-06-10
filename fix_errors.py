#!/usr/bin/env python3

import re

# Read the file
with open('framework.html', 'r') as f:
    content = f.read()

# Fix G3.5 - Remove evidence column from row c 
content = re.sub(
    r'(\s+<td>c\. Establish proactive response strategies and scenarios for maintaining AAI operational security\.</td>\s+<td class="sfr-align">N</td>\s+<td class="sfr-align">D, I, O, M, R</td>)\s+<td>.*?(?=</td>\s*</tr>)',
    r'\1',
    content,
    flags=re.DOTALL
)

# Fix G3.6 - Remove evidence column from row d
content = re.sub(
    r'(\s+<td>d\. Implement robust human override capabilities to ensure final authority remains with human operators\.</td>\s+<td class="sfr-align">N</td>\s+<td class="sfr-align">D, I, O, M, R</td>)\s+<td>.*?(?=</td>\s*</tr>)',
    r'\1',
    content,
    flags=re.DOTALL
)

# Fix G3.7 - Remove evidence column from row c
content = re.sub(
    r'(\s+<td>c\. Establish internal identification and validation protocols when global standards are not available\.</td>\s+<td class="sfr-align">N</td>\s+<td class="sfr-align">D, I, O, M, R</td>)\s+<td>.*?(?=</td>\s*</tr>)',
    r'\1',
    content,
    flags=re.DOTALL
)

# Fix G3.1b - Remove evidence column from row c
content = re.sub(
    r'(\s+<td>c\. Establish safeguards against poisoning in dynamic model ensembles and expert systems\.</td>\s+<td class="sfr-align">N</td>\s+<td class="sfr-align">D, I, O, M, R</td>)\s+<td>.*?(?=</td>\s*</tr>)',
    r'\1',
    content,
    flags=re.DOTALL
)

# Fix G3.2b - Remove evidence column from row b
content = re.sub(
    r'(\s+<td>b\. Establish comprehensive data assurance protocols to prevent malicious manipulation of training datasets\.</td>\s+<td class="sfr-align">N</td>\s+<td class="sfr-align">D, I, O, M, R</td>)\s+<td>.*?(?=</td>\s*</tr>)',
    r'\1',
    content,
    flags=re.DOTALL
)

# Fix G3.3b - Remove evidence column from row c
content = re.sub(
    r'(\s+<td>c\. Establish operational continuity plans for ecosystem-wide infection scenarios\.</td>\s+<td class="sfr-align">N</td>\s+<td class="sfr-align">D, I, O, M, R</td>)\s+<td>.*?(?=</td>\s*</tr>)',
    r'\1',
    content,
    flags=re.DOTALL
)

# Fix G3.4b - Remove evidence column from row b
content = re.sub(
    r'(\s+<td>b\. Maintain dynamic vulnerability tracking and patch management systems, and establish protection protocols for privileged information to prevent unauthorized control of AAI systems\.</td>\s+<td class="sfr-align">N</td>\s+<td class="sfr-align">D, I, O, M, R</td>)\s+<td>.*?(?=</td>\s*</tr>)',
    r'\1',
    content,
    flags=re.DOTALL
)

# Fix G3.5b - Remove evidence column from row b
content = re.sub(
    r'(\s+<td>b\. Implement adaptable policies that maintain AAI ecosystem integrity across international boundaries\.</td>\s+<td class="sfr-align">N</td>\s+<td class="sfr-align">D, I, O, M, R</td>)\s+<td>.*?(?=</td>\s*</tr>)',
    r'\1',
    content,
    flags=re.DOTALL
)

# Write the corrected content back
with open('framework.html', 'w') as f:
    f.write(content)

print("Fixed all identified table errors!") 