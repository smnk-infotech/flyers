#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import sys

files = [
    "About Us – Flyers Charitable Trust.html",
    "Services – Flyers Charitable Trust.html",
    "Gallery – Flyers Charitable Trust.html",
    "Donation – Flyers Charitable Trust.html",
    "Contact US – Flyers Charitable Trust.html"
]

old_menu = '''<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-352"><a href="About Us – Flyers Charitable Trust.html" class="elementor-item menu-link">About Us</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-364"><a href="Services – Flyers Charitable Trust.html" class="elementor-item menu-link">Services</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-561"><a href="Donation – Flyers Charitable Trust.html" class="elementor-item menu-link">Donation</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-360"><a href="Gallery – Flyers Charitable Trust.html" class="elementor-item menu-link">Gallery</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-359"><a href="Contact US – Flyers Charitable Trust.html" class="elementor-item menu-link">Contact Us</a></li>'''

new_menu = '''<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-352"><a href="About Us – Flyers Charitable Trust.html" class="elementor-item menu-link elementor-item-anchor">About Us</a>
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

# Tabindex version
old_menu_tab = old_menu.replace('class="elementor-item menu-link">', 'class="elementor-item menu-link" tabindex="-1">')
new_menu_tab = new_menu.replace('class="elementor-item menu-link">', 'class="elementor-item menu-link" tabindex="-1">').replace('class="elementor-sub-item menu-link">', 'class="elementor-sub-item menu-link" tabindex="-1">')

for file in files:
    try:
        print(f"Processing {file}...")
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Replace both versions
        content = content.replace(old_menu, new_menu)
        content = content.replace(old_menu_tab, new_menu_tab)
        
        if content != original_content:
            with open(file, 'w', encoding='utf-8', newline='') as f:
                f.write(content)
            print(f"  ✓ Updated {file}")
        else:
            print(f"  - No changes needed for {file}")
            
    except Exception as e:
        print(f"  ✗ Error processing {file}: {e}", file=sys.stderr)

print("\n✓ All files processed!")
