import re

def fix_next_batch():
    with open('framework.html', 'r') as f:
        content = f.read()
    
    print("Starting fixes...")
    
    # Fix G4.3b - Failed Super-alignment (4 SFRs with all I values)
    if 'Implement monitoring systems to detect and evaluate changes in self-improving AI value systems' in content:
        content = re.sub(
            r'(<td>a\. Implement monitoring systems to detect and evaluate changes in self-improving AI value systems, particularly during autonomous learning\.)<br><br>(b\. Establish comprehensive risk assessment frameworks for identifying emergence of non-human value systems\.)<br><br>(c\. Develop response protocols for managing detected value system divergences\.)<br><br>(d\. Monitor for subtle shifts in value interpretation that may indicate growing misalignment with human values\.)</td>\s*<td>I<br><br>I<br><br>I<br><br>I</td>',
            r'\1</td>\n                    <td class="sfr-align">I</td>\n                    <td class="sfr-align">D, I, O, M, R</td>\n                    <td rowspan="4">I. Documentation of methodologies used to identify and track value system changes, including detection of potential divergence from human values.<br><br>II. Detailed risk assessment criteria and scoring systems for evaluating identified changes in AI value systems.<br><br>III. Standard operating procedures for responding to different types and levels of value system risks.</td>\n                </tr>\n                <tr>\n                    <td>\2</td>\n                    <td class="sfr-align">I</td>\n                    <td class="sfr-align">D, I, O, M, R</td>\n                </tr>\n                <tr>\n                    <td>\3</td>\n                    <td class="sfr-align">I</td>\n                    <td class="sfr-align">D, I, O, M, R</td>\n                </tr>\n                <tr>\n                    <td>\4</td>\n                    <td class="sfr-align">I</td>\n                    <td class="sfr-align">D, I, O, M, R</td>',
            content
        )
        print("Fixed G4.3b")
    
    # Fix G4.4b - Temporal Changes in Societal Values (4 SFRs)
    if 'Implement processes to detect and evaluate meaningful changes in societal values' in content:
        content = re.sub(
            r'(<td>a\. Implement processes to detect and evaluate meaningful changes in societal values and norms across multiple scales and domains\.)<br><br>(b\. Develop mechanisms to prevent AI systems from operating with obsolete value frameworks\.)<br><br>(c\. Establish protocols for updating value codices while maintaining system stability and consistency\.)<br><br>(d\. Maintain transparent documentation of value system evolution and updates\.)</td>\s*<td>N<br><br>N<br><br>I<br><br>I</td>',
            r'\1</td>\n                    <td class="sfr-align">N</td>\n                    <td class="sfr-align">D, I, O, M, R</td>\n                    <td rowspan="4">I. Documentation of methodologies used to identify significant changes in societal values, including thresholds for action.<br><br>II. Technical specifications showing implementation of controls preventing use of outdated norms.<br><br>III. Process documentation for value codex updates, including triggering conditions and verification procedures.<br><br>IV. System logs tracking all modifications to value frameworks, including justifications and impact assessments.</td>\n                </tr>\n                <tr>\n                    <td>\2</td>\n                    <td class="sfr-align">N</td>\n                    <td class="sfr-align">D, I, O, M, R</td>\n                </tr>\n                <tr>\n                    <td>\3</td>\n                    <td class="sfr-align">I</td>\n                    <td class="sfr-align">D, I, O, M, R</td>\n                </tr>\n                <tr>\n                    <td>\4</td>\n                    <td class="sfr-align">I</td>\n                    <td class="sfr-align">D, I, O, M, R</td>',
            content
        )
        print("Fixed G4.4b")
    
    # Fix G4.5b - Systemic Value Dilution (3 SFRs)
    if 'Implement comprehensive verification processes to verify ongoing fidelity' in content:
        content = re.sub(
            r'(<td>a\. Implement comprehensive verification processes to verify ongoing fidelity of encoded values\.)<br><br>(b\. Develop methods to detect degradation in value system implementation, particularly during multi-step reasoning processes\.)<br><br>(c\. Establish monitoring systems for value preservation across different learning and operational pathways\.)</td>\s*<td>N<br><br>N<br><br>I</td>',
            r'\1</td>\n                    <td class="sfr-align">N</td>\n                    <td class="sfr-align">D, I, O, M, R</td>\n                    <td rowspan="3">I. Documentation of test plans and scripts designed to detect value dilution, including: Edge case testing procedures, multi-step reasoning verification, and value preservation assessments.<br><br>II. System logs demonstrating: Regular value fidelity testing, detection of potential value degradation, and corrective actions taken.</td>\n                </tr>\n                <tr>\n                    <td>\2</td>\n                    <td class="sfr-align">N</td>\n                    <td class="sfr-align">D, I, O, M, R</td>\n                </tr>\n                <tr>\n                    <td>\3</td>\n                    <td class="sfr-align">I</td>\n                    <td class="sfr-align">D, I, O, M, R</td>',
            content
        )
        print("Fixed G4.5b")
    
    # Fix G5 - Main Transparency table (4 SFRs)
    if 'Implement clear and accessible explanations for AI-generated outputs' in content:
        content = re.sub(
            r'(<td>a\. Implement clear and accessible explanations for AI-generated outputs and decisions, ensuring human interpretability across various user expertise levels\.)<br><br>(b\. Develop and maintain comprehensive documentation of the AI model\'s development process, including data collection, preprocessing, architecture, and training methodologies\.)<br><br>(c\. Establish robust auditing and review processes to continually assess and improve the transparency and explainability of the AI system\.)<br><br>(d\. Create and implement user feedback mechanisms to enhance the understandability and relevance of AI explanations\.)</td>\s*<td>N<br><br>N<br><br>N<br><br>I</td>',
            r'\1</td>\n                    <td class="sfr-align">N</td>\n                    <td class="sfr-align">D, I, O, M, R</td>\n                    <td rowspan="4">I. Formal transparency and explainability policies.<br><br>II. Detailed algorithmic design documentation.<br><br>III. Complete model specs with training and testing results.<br><br>IV. Training and verification datasets System execution logs and monitoring records.<br><br>V. Internal guidelines for AI-generated content explanations.<br><br>VI. Comprehensive development process documentation showing compliance.<br><br>VII. Internal and external audit findings with subsequent improvements.<br><br>VIII. Case studies demonstrating decision-making processes, and records of stakeholder engagement and feedback incorporation.<br><br>IX. User guides with layered explanations for different expertise levels, and documentation of content moderation and safety measures.<br><br>X. Evidence showing how user feedback improves system understandability.</td>\n                </tr>\n                <tr>\n                    <td>\2</td>\n                    <td class="sfr-align">N</td>\n                    <td class="sfr-align">D, I, O, M, R</td>\n                </tr>\n                <tr>\n                    <td>\3</td>\n                    <td class="sfr-align">N</td>\n                    <td class="sfr-align">D, I, O, M, R</td>\n                </tr>\n                <tr>\n                    <td>\4</td>\n                    <td class="sfr-align">I</td>\n                    <td class="sfr-align">D, I, O, M, R</td>',
            content
        )
        print("Fixed G5")
    
    # Fix G5.1 - Logging of Internal Goals (4 SFRs)
    if 'Maintain detailed real-time logs of all internal goals' in content:
        content = re.sub(
            r'(<td>a\. Maintain detailed real-time logs of all internal goals, including their initial formations, modifications, and completed states\.)<br><br>(b\. Implement clear mechanisms to maintain goal alignment during learning and environmental changes\.)<br><br>(c\. Generate alerts for all self-learning events\.)<br><br>(d\. Record and analyze goal-related transformations\.)</td>\s*<td>N<br><br>N<br><br>I<br><br>I</td>',
            r'\1</td>\n                    <td class="sfr-align">N</td>\n                    <td class="sfr-align">D, I, O, M, R</td>\n                    <td rowspan="4">I. Comprehensive documentation including goal management policies and procedures, verified specifications of internal goals, system architecture for goal-related logging, and detailed alert generation mechanisms.<br><br>II. Operational records demonstrating complete logging of goal formation and evolution, audit trails of transformations and triggers, alert responses and analysis reports, and case studies of goal adaptations.<br><br>III. Technical implementation evidence including goal alignment algorithms, optimization methods, internal feedback loop mechanisms, and system validation results.</td>\n                </tr>\n                <tr>\n                    <td>\2</td>\n                    <td class="sfr-align">N</td>\n                    <td class="sfr-align">D, I, O, M, R</td>\n                </tr>\n                <tr>\n                    <td>\3</td>\n                    <td class="sfr-align">I</td>\n                    <td class="sfr-align">D, I, O, M, R</td>\n                </tr>\n                <tr>\n                    <td>\4</td>\n                    <td class="sfr-align">I</td>\n                    <td class="sfr-align">D, I, O, M, R</td>',
            content
        )
        print("Fixed G5.1")
    
    with open('framework.html', 'w') as f:
        f.write(content)
    
    print("Done with this batch!")

if __name__ == "__main__":
    fix_next_batch() 