import codecs
import os
import re

base_path = r"c:\Users\smnk2\Downloads\flyers"

# All HTML files that need fixes
html_files = [
    "Flyers Charitable Trust – Flyers Charitable Trust In Coimbatore.html",
    "About Us – Flyers Charitable Trust.html",
    "Services – Flyers Charitable Trust.html",
    "Gallery – Flyers Charitable Trust.html",
    "Contact US – Flyers Charitable Trust.html",
    "Donation – Flyers Charitable Trust.html",
    "Know-Us.html",
    "Milestone.html",
    "Our-Partners.html",
    "Our-Story-Team.html",
    "Testimonial.html",
    "Transparency.html",
    "Privacy Policy – Flyers Charitable Trust.html",
    "Terms & Conditions – Flyers Charitable Trust.html"
]

print("Fixing remaining issues...")
print()

for filename in html_files:
    file_path = os.path.join(base_path, filename)
    
    if not os.path.exists(file_path):
        print(f"✗ {filename} - File not found")
        continue
    
    with codecs.open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    changes = []
    
    # Fix 1: Add fixes.css if missing (for Privacy Policy and Terms pages)
    if 'fixes.css' not in content:
        # Find the </head> tag and insert before it
        if '</head>' in content:
            content = content.replace('</head>', '<link rel="stylesheet" href="./fixes.css" media="all">\n</head>')
            changes.append("Added fixes.css link")
    
    # Fix 2: Add logo alt text if missing
    # Pattern: <img ... class="..." (without alt or with empty alt) before or after "logo"
    
    # Find all logo images without proper alt text
    logo_pattern = r'(<img[^>]+(?:logo\.jpg|class="[^"]*logo[^"]*")[^>]*?)(?:\s+alt=""\s*|\s+(?!alt)([^>]*?))(/?>)'
    
    def fix_logo_alt(match):
        before = match.group(1)
        middle = match.group(2) if match.group(2) else ''
        after = match.group(3)
        
        # Check if alt already exists with proper text
        if 'alt="Flyers Charitable Trust' in before:
            return match.group(0)  # Already has proper alt
        
        # Remove any existing empty alt=""
        before = re.sub(r'\s+alt=""', '', before)
        
        # Add proper alt text
        if middle:
            return f'{before} alt="Flyers Charitable Trust Logo" {middle}{after}'
        else:
            return f'{before} alt="Flyers Charitable Trust Logo"{after}'
    
    # Apply logo alt fix
    new_content = re.sub(logo_pattern, fix_logo_alt, content, flags=re.IGNORECASE)
    
    if new_content != content:
        changes.append("Fixed logo alt text")
        content = new_content
    
    # Write back if changes were made
    if changes:
        with codecs.open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✓ {filename}")
        for change in changes:
            print(f"  - {change}")
    else:
        print(f"• {filename} - Already correct")

print()
print("✅ All fixes applied!")
