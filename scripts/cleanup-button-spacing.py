#!/usr/bin/env python3
"""Clean up button styling - remove unnecessary margin-right since flexbox gap handles spacing"""

import re

pages = [
    'About Us – Flyers Charitable Trust.html',
    'Services – Flyers Charitable Trust.html',
    'Gallery – Flyers Charitable Trust.html',
    'Donation – Flyers Charitable Trust.html',
    'Contact US – Flyers Charitable Trust.html'
]

count = 0
for page in pages:
    try:
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Remove the redundant margin-right since flexbox gap handles spacing
        # Pattern: ;; margin-right: 10px; or ; margin-right: 10px;
        content = re.sub(
            r'(transition: all 0\.25s ease);[; ]*margin-right: 10px;',
            r'\1;',
            content
        )
        
        if content != original_content:
            with open(page, 'w', encoding='utf-8', newline='') as f:
                f.write(content)
            print(f'✓ Cleaned up {page}')
            count += 1
        else:
            print(f'⚠ No cleanup needed for {page}')
            
    except FileNotFoundError:
        print(f'✗ File not found: {page}')
    except Exception as e:
        print(f'✗ Error with {page}: {e}')

print(f'\n✅ Cleanup complete! Fixed {count} pages.')
print('Buttons now use flexbox gap for proper spacing.')
