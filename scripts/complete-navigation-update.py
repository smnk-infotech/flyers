# -*- coding: utf-8 -*-
"""
Complete navigation update script for all remaining pages
Updates menu structure and buttons on 5 HTML files
"""

import re
import sys

# Files to update
pages = [
    "About Us – Flyers Charitable Trust.html",
    "Services – Flyers Charitable Trust.html",
    "Gallery – Flyers Charitable Trust.html",
    "Donation – Flyers Charitable Trust.html",
    "Contact US – Flyers Charitable Trust.html"
]

# Old menu pattern (simple replacement)
old_menu_items = [
    '<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-352"><a href="About Us – Flyers Charitable Trust.html" class="elementor-item menu-link">About Us</a></li>',
    '<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-364"><a href="Services – Flyers Charitable Trust.html" class="elementor-item menu-link">Services</a></li>',
    '<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-561"><a href="Donation – Flyers Charitable Trust.html" class="elementor-item menu-link">Donation</a></li>',
    '<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-360"><a href="Gallery – Flyers Charitable Trust.html" class="elementor-item menu-link">Gallery</a></li>',
    '<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-359"><a href="Contact US – Flyers Charitable Trust.html" class="elementor-item menu-link">Contact Us</a></li>'
]

# New menu items
new_menu_items = '''<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-352"><a href="About Us – Flyers Charitable Trust.html" class="elementor-item menu-link elementor-item-anchor">About Us</a>
<ul class="sub-menu elementor-nav-menu--dropdown">
<li class="menu-item menu-item-type-custom menu-item-object-custom"><a href="About Us – Flyers Charitable Trust.html#know-us" class="elementor-sub-item menu-link">Know Us</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom"><a href="About Us – Flyers Charitable Trust.html#our-story" class="elementor-sub-item menu-link">Our Story & Team</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom"><a href="About Us – Flyers Charitable Trust.html#milestone" class="elementor-sub-item menu-link">Milestone</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom"><a href="About Us – Flyers Charitable Trust.html#our-partners" class="elementor-sub-item menu-link">Our Partners</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom"><a href="About Us – Flyers Charitable Trust.html#transparency" class="elementor-sub-item menu-link">Transparency</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom"><a href="About Us – Flyers Charitable Trust.html#testimonial" class="elementor-sub-item menu-link">Testimonial</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom"><a href="Contact US – Flyers Charitable Trust.html" class="elementor-sub-item menu-link">Contact Us</a></li>
</ul>
</li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-364"><a href="Services – Flyers Charitable Trust.html" class="elementor-item menu-link">Programs</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-561"><a href="Services – Flyers Charitable Trust.html#impact" class="elementor-item menu-link">Impact</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-360"><a href="Gallery – Flyers Charitable Trust.html" class="elementor-item menu-link">Gallery</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-362"><a href="Services – Flyers Charitable Trust.html#volunteer" class="elementor-item menu-link">Volunteer</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-363"><a href="Services – Flyers Charitable Trust.html#csr" class="elementor-item menu-link">CSR</a></li>'''

def update_page(filename):
    """Update a single HTML page"""
    print(f"\n📄 Processing {filename}...")
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes = 0
        
        # Replace old menu items with new ones
        old_pattern = '\n'.join(old_menu_items)
        if old_pattern in content:
            content = content.replace(old_pattern, new_menu_items)
            menu_count = original_content.count(old_pattern)
            changes += menu_count
            print(f"   ✓ Updated {menu_count} menu instance(s)")
        
        # Also handle tabindex versions for mobile menus
        old_pattern_mobile = old_pattern.replace('class="elementor-item menu-link"', 'class="elementor-item menu-link" tabindex="-1"')
        new_pattern_mobile = new_menu_items.replace('class="elementor-sub-item menu-link"', 'class="elementor-sub-item menu-link" tabindex="-1"')
        new_pattern_mobile = new_pattern_mobile.replace('class="elementor-item menu-link"', 'class="elementor-item menu-link" tabindex="-1"')
        new_pattern_mobile = new_pattern_mobile.replace('class="elementor-item menu-link elementor-item-anchor"', 'class="elementor-item menu-link elementor-item-anchor" tabindex="-1"')
        
        if old_pattern_mobile in content:
            content = content.replace(old_pattern_mobile, new_pattern_mobile)
            mobile_count = content.count(new_pattern_mobile) - changes
            changes += mobile_count  
            print(f"   ✓ Updated {mobile_count} mobile menu instance(s)")
        
        # Update Corporate Portal buttons
        button_changes = 0
        
        # Replace button text
        content = content.replace('<span class="elementor-button-text">Corporate Portal</span>', 
                                   '<span class="elementor-button-text">Donate Now</span>')
        button_changes += (original_content.count('Corporate Portal') - content.count('Corporate Portal'))
        
        # Replace button icon
        content = content.replace('<i aria-hidden="true" class="fas fa-user-circle"></i>', 
                                   '<i aria-hidden="true" class="fas fa-heart"></i>')
        
        # Replace button links
        content = content.replace('href="/portal/login?redirect=/"', 'href="Donation – Flyers Charitable Trust.html"')
        content = content.replace('href="/portal/login"', 'href="Donation – Flyers Charitable Trust.html"')
        
        if button_changes > 0:
            print(f"   ✓ Updated {button_changes} button(s)")
            changes += button_changes
        
        # Write back
        if content != original_content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"   ✅ {filename} - {changes} total change(s)")
            return True
        else:
            print(f"   ⚠️  No changes needed")
            return False
            
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False

def main():
    print("=" * 70)
    print("🚀 Navigation Update Script")
    print("=" * 70)
    
    updated = 0
    for page in pages:
        if update_page(page):
            updated += 1
    
    print("\n" + "=" * 70)
    print(f"✅ Completed! {updated}/{len(pages)} page(s) updated successfully")
    print("=" * 70)
    print("\n📋 Updates Applied:")
    print("   • Navigation menu with About Us dropdown (7 sub-items)")
    print("   • Replaced 'Corporate Portal' with 'Donate Now' button")
    print("   • Changed icon from fa-user-circle to fa-heart")
    print("   • Updated button links to Donation page")
    print("\n🔍 Test the changes:")
    print("   • Open http://localhost:8000 in your browser")
    print("   • Navigate to each updated page")
    print("   • Test dropdown menu on desktop")
    print("   • Test mobile menu responsiveness")
    print()

if __name__ == '__main__':
    main()
