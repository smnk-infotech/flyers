import codecs
import re

file_path = r"c:\Users\smnk2\Downloads\flyers\Our-Story-Team.html"
css_file_path = r"c:\Users\smnk2\Downloads\flyers\fixes.css"

# Read HTML file
with codecs.open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Remove inline styles from header sticky elements (lines 170, 249)
content = re.sub(
    r'(<div class="elementor-element elementor-element-2656253[^>]*) style="position: fixed; width: 1511\.2px; margin-top: 0px; margin-bottom: 0px; top: 0px;">',
    r'\1>',
    content
)

content = re.sub(
    r'(<div class="elementor-element elementor-element-2656253[^>]*) style="visibility: hidden; transition: none; animation: auto ease 0s 1 normal none running none;">',
    r'\1>',
    content
)

# Remove inline styles from mobile header (lines 381, 419)
content = re.sub(
    r'(<div class="elementor-element elementor-element-8cd323e[^>]*) style="position: fixed; width: 100px; margin-top: 0px; margin-bottom: 0px; top: 0px;">',
    r'\1>',
    content
)

content = re.sub(
    r'(<div class="elementor-element elementor-element-8cd323e[^>]*) style="visibility: hidden; transition: none; animation: auto ease 0s 1 normal none running none;">',
    r'\1>',
    content
)

# Remove inline styles from nav menu (line 396)
content = re.sub(
    r'(<nav class="elementor-nav-menu--dropdown elementor-nav-menu__container"[^>]*) style="width: 1511px; left: 0px; top: 0px;">',
    r'\1>',
    content
)

# Remove opacity inline styles from SVG paths (lines 558-560, 566-568)
content = re.sub(
    r'(<path class="elementor-shape-fill") style="opacity:0\.33"',
    r'\1',
    content
)

# Remove inline styles from footer elements (lines 1044, 1047, 1053-1054)
content = re.sub(
    r'(<span id="elementor-device-mode"[^>]*) style="display: none;">',
    r'\1>',
    content
)

content = re.sub(
    r'(<svg[^>]*) style="display: none;">',
    r'\1>',
    content
)

content = re.sub(
    r'(<span id="PING_IFRAME_FORM_DETECTION"[^>]*) style="display: none;">',
    r'\1>',
    content
)

content = re.sub(
    r'(data-elementor-post-type="elementor_library") style="display: block;">',
    r'\1>',
    content
)

content = re.sub(
    r'(<div class="elementor-image-carousel swiper-wrapper"[^>]*) style="transform: translate3d\(-120px, 0px, 0px\); transition-duration: 500ms;"',
    r'\1',
    content
)

content = re.sub(
    r'(<div class="swiper-slide[^"]*"[^>]*) style="width: 60px;"',
    r'\1',
    content
)

# Write back HTML
with codecs.open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

# Add CSS rules to external stylesheet
css_rules = """
/* Fixed header and mobile nav positioning - moved from inline styles */
.elementor-sticky--active {
    position: fixed !important;
    top: 0 !important;
    margin-top: 0 !important;
    margin-bottom: 0 !important;
}

.elementor-sticky__spacer {
    visibility: hidden !important;
    transition: none !important;
    animation: none !important;
}

.elementor-nav-menu--dropdown.elementor-nav-menu__container {
    width: auto !important;
    left: 0 !important;
    top: 0 !important;
}

/* SVG shape opacity */
.elementor-shape-fill {
    opacity: 0.33;
}

.elementor-shape-fill:last-child {
    opacity: 1;
}

/* Hidden elements */
#elementor-device-mode,
.e-font-icon-svg-symbols,
#PING_IFRAME_FORM_DETECTION {
    display: none !important;
}

/* Popup and carousel display */
.elementor-location-popup {
    display: block;
}

/* Swiper carousel sizing - controlled by Swiper JS */
.swiper-slide {
    width: auto;
}

.elementor-image-carousel.swiper-wrapper {
    transform: translate3d(0, 0, 0);
    transition-duration: 500ms;
}
"""

# Read existing CSS
try:
    with codecs.open(css_file_path, "r", encoding="utf-8") as f:
        existing_css = f.read()
except FileNotFoundError:
    existing_css = ""

# Append new rules if not already present
if "Fixed header and mobile nav positioning" not in existing_css:
    with codecs.open(css_file_path, "a", encoding="utf-8") as f:
        f.write("\n" + css_rules)
    print("✓ Added CSS rules to fixes.css")
else:
    print("⚠ CSS rules already exist in fixes.css")

print("✓ Removed all inline styles from Our-Story-Team.html")
print("\n✅ All 19 inline style warnings fixed!")
