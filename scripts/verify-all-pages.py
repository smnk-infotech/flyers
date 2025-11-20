import codecs
import os
import re

# List of all main pages to verify
pages = [
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

base_path = r"c:\Users\smnk2\Downloads\flyers"

print("=" * 70)
print("FLYERS CHARITABLE TRUST - WEBSITE VERIFICATION")
print("=" * 70)
print()

total_pages = len(pages)
verified_pages = 0
issues_found = []

for page in pages:
    file_path = os.path.join(base_path, page)
    
    if not os.path.exists(file_path):
        print(f"✗ {page}")
        print(f"  ERROR: File not found")
        issues_found.append(f"{page}: File not found")
        continue
    
    # Read the file
    try:
        with codecs.open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Verify fixes.css is linked
        has_fixes_css = 'href="./fixes.css"' in content or 'href="fixes.css"' in content
        
        # Check for inline styles (should be minimal/none for buttons)
        inline_button_styles = len(re.findall(r'<a[^>]*style="[^"]*"[^>]*class="[^"]*btn-', content))
        
        # Check for charset
        has_correct_charset = '<meta charset="UTF-8">' in content
        
        # Check for logo alt text (only if logo images exist)
        logo_imgs = re.findall(r'<img[^>]*logo\.jpg[^>]*>', content, re.IGNORECASE)
        if logo_imgs:
            has_logo_alt = any('alt="Flyers Charitable Trust' in img for img in logo_imgs)
            if not has_logo_alt:
                page_issues.append("Missing logo alt text")
        # If no logo images, that's OK (some pages like Privacy Policy don't have them)
        
        # Check page title
        title_match = re.search(r'<title>([^<]+)</title>', content)
        page_title = title_match.group(1) if title_match else "No title"
        
        # Summary
        page_issues = []
        if not has_fixes_css:
            page_issues.append("Missing fixes.css link")
        if inline_button_styles > 0:
            page_issues.append(f"{inline_button_styles} inline button styles")
        if not has_correct_charset:
            page_issues.append("Missing UTF-8 charset")
        
        # Logo alt check moved above
        
        if page_issues:
            print(f"⚠ {page}")
            print(f"  Title: {page_title}")
            for issue in page_issues:
                print(f"  - {issue}")
            issues_found.extend([f"{page}: {issue}" for issue in page_issues])
        else:
            print(f"✓ {page}")
            print(f"  Title: {page_title}")
            verified_pages += 1
        
    except Exception as e:
        print(f"✗ {page}")
        print(f"  ERROR: {str(e)}")
        issues_found.append(f"{page}: {str(e)}")
    
    print()

# Final summary
print("=" * 70)
print("VERIFICATION SUMMARY")
print("=" * 70)
print(f"Total pages checked: {total_pages}")
print(f"Pages verified: {verified_pages}")
print(f"Pages with issues: {total_pages - verified_pages}")
print()

if issues_found:
    print("ISSUES FOUND:")
    for issue in issues_found:
        print(f"  • {issue}")
    print()
else:
    print("✅ ALL PAGES VERIFIED SUCCESSFULLY!")
    print()

print("Server running at: http://localhost:8000")
print()
print("Key pages to test:")
print("  • Home: http://localhost:8000/Flyers%20Charitable%20Trust%20%E2%80%93%20Flyers%20Charitable%20Trust%20In%20Coimbatore.html")
print("  • About Us: http://localhost:8000/About%20Us%20%E2%80%93%20Flyers%20Charitable%20Trust.html")
print("  • Our Story & Team: http://localhost:8000/Our-Story-Team.html")
print("  • Services: http://localhost:8000/Services%20%E2%80%93%20Flyers%20Charitable%20Trust.html")
print("  • Contact: http://localhost:8000/Contact%20US%20%E2%80%93%20Flyers%20Charitable%20Trust.html")
print("=" * 70)
