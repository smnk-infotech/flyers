#!/usr/bin/env python3
"""Fix Portal Login button layout to be side-by-side with Donate Now button"""

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
        
        # Pattern 1: Add flexbox to button wrapper and remove margin-right from Donate button
        # Replace: <div class="elementor-button-wrapper">
        # With: <div class="elementor-button-wrapper" style="display: flex; gap: 10px; align-items: center; justify-content: flex-end;">
        content = re.sub(
            r'<div class="elementor-button-wrapper">',
            r'<div class="elementor-button-wrapper" style="display: flex; gap: 10px; align-items: center; justify-content: flex-end;">',
            content
        )
        
        # Pattern 2: Remove margin-right from Donate Now buttons
        content = re.sub(
            r'(href="Donation – Flyers Charitable Trust\.html" style="background: linear-gradient\(135deg, #060097 0%, #0800c4 100%\); color: #ffffff; padding: 12px 20px; font-weight: 600; border-radius: 6px; box-shadow: 0 4px 12px rgba\(6, 0, 151, 0\.18\); transition: all 0\.25s ease); margin-right: 10px;"',
            r'\1;"',
            content
        )
        
        if content != original_content:
            with open(page, 'w', encoding='utf-8', newline='') as f:
                f.write(content)
            print(f'✓ Updated {page} - Buttons now display side-by-side')
            count += 1
        else:
            print(f'⚠ No changes needed for {page}')
            
    except FileNotFoundError:
        print(f'✗ File not found: {page}')
    except Exception as e:
        print(f'✗ Error with {page}: {e}')

print(f'\n✅ Layout fix complete! Updated {count} pages.')
print('Buttons will now display horizontally side-by-side using flexbox.')
