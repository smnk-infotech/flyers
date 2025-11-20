import os
import re

def update_links():
    # Define the replacements
    replacements = {
        'href="About Us – Flyers Charitable Trust.html#know-us"': 'href="Know-Us.html"',
        'href="About Us – Flyers Charitable Trust.html#our-story"': 'href="Our-Story-Team.html"',
        'href="About Us – Flyers Charitable Trust.html#milestone"': 'href="Milestone.html"',
        'href="About Us – Flyers Charitable Trust.html#our-partners"': 'href="Our-Partners.html"',
        'href="About Us – Flyers Charitable Trust.html#transparency"': 'href="Transparency.html"',
        'href="About Us – Flyers Charitable Trust.html#testimonial"': 'href="Testimonial.html"',
        # Also handle cases where it might be encoded or have different spacing if necessary
        # But based on grep, the above should cover it.
    }

    # List of files to update
    files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    print(f"Found {len(files)} HTML files to check.")

    for filename in files:
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            changes_made = False
            
            for old_link, new_link in replacements.items():
                if old_link in content:
                    content = content.replace(old_link, new_link)
                    changes_made = True
            
            if changes_made:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ Updated links in {filename}")
            else:
                print(f"⚠ No changes needed for {filename}")
                
        except Exception as e:
            print(f"❌ Error processing {filename}: {e}")

if __name__ == "__main__":
    update_links()
