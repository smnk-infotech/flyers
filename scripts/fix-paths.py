#!/usr/bin/env python3
"""Fix asset path encoding issues in HTML files."""

import os
import glob

def fix_paths():
    # Change to script's parent directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    site_root = os.path.dirname(script_dir)
    os.chdir(site_root)
    
    # Bad sequence: â€" (mis-decoded UTF-8 en-dash bytes interpreted as Windows-1252)
    bad_seq = '\u00e2\u20ac\u201c'  # â€"
    correct_dash = '\u2013'  # –
    
    html_files = [f for f in glob.glob('*.html') if '_files' not in f]
    
    fixed_count = 0
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if bad_seq in content:
            new_content = content.replace(bad_seq, correct_dash)
            with open(filepath, 'w', encoding='utf-8', newline='') as f:
                f.write(new_content)
            print(f'✓ Fixed: {filepath}')
            fixed_count += 1
    
    print(f'\nFixed {fixed_count} file(s).')

if __name__ == '__main__':
    fix_paths()
