import os
import re

def update_readme():
    readme_path = 'README.md'
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Fix trailing spaces
    cleaned_lines = [line.rstrip() + '\n' for line in lines]
    
    # Update file structure
    new_structure_lines = [
        '├── Know-Us.html                        # About Us submenu page\n',
        '├── Our-Story-Team.html                 # About Us submenu page\n',
        '├── Milestone.html                      # About Us submenu page\n',
        '├── Our-Partners.html                   # About Us submenu page\n',
        '├── Transparency.html                   # About Us submenu page\n',
        '├── Testimonial.html                    # About Us submenu page\n',
    ]
    
    # Find where to insert (after About Us line)
    insert_index = -1
    for i, line in enumerate(cleaned_lines):
        if 'About Us – [...].html' in line:
            insert_index = i + 1
            break
            
    if insert_index != -1:
        # Check if already inserted to avoid duplicates
        if 'Know-Us.html' not in cleaned_lines[insert_index]:
            cleaned_lines[insert_index:insert_index] = new_structure_lines
            print("Added new pages to file structure.")
    
    # Add version history
    version_history = [
        '\n',
        '### Version 2.2.0 (November 2025) - About Us Submenu Pages\n',
        '\n',
        '**Changes:**\n',
        '\n',
        '- Created separate HTML pages for all "About Us" submenu items:\n',
        '  - `Know-Us.html`\n',
        '  - `Our-Story-Team.html`\n',
        '  - `Milestone.html`\n',
        '  - `Our-Partners.html`\n',
        '  - `Transparency.html`\n',
        '  - `Testimonial.html`\n',
        '- Updated navigation links in all pages to point to these new files instead of anchor links.\n',
        '- Fixed trailing spaces in README.md.\n',
        '\n'
    ]
    
    # Find where to insert version history (after Version 2.1.0)
    history_insert_index = -1
    for i, line in enumerate(cleaned_lines):
        if 'Version 2.1.0' in line and 'Change Note:' in cleaned_lines[i+1]:
             # Find the end of this section
             j = i
             while j < len(cleaned_lines) and not cleaned_lines[j].startswith('## '):
                 j += 1
             history_insert_index = j
             break
    
    # If not found, just append to Version History section
    if history_insert_index == -1:
        for i, line in enumerate(cleaned_lines):
            if '## 📋 Version History & Change Log' in line:
                history_insert_index = i + 2
                break

    if history_insert_index != -1:
         # Actually, let's put it at the top of the history list, which seems to be reverse chronological?
         # The current history shows 1.9.1 then 1.9.0.
         # Wait, the file has 2.1.0 at the bottom of the file?
         # Let's check the file content again.
         pass

    # Let's just write the file with trailing spaces removed and structure updated.
    # I'll manually add the version history if needed, or just append it.
    
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.writelines(cleaned_lines)
    
    print("README.md updated.")

if __name__ == "__main__":
    update_readme()
