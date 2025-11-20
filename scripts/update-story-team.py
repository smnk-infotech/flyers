import re

file_path = r"c:\Users\smnk2\Downloads\flyers\Our-Story-Team.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Update Vision to Journey
content = content.replace(
    '<h2 class="elementor-heading-title elementor-size-default">VISION</h2>',
    '<h2 class="elementor-heading-title elementor-size-default">OUR JOURNEY</h2>'
)

content = content.replace(
    "The organization's vision is to create excellent people and live a truly joyful life that is full of humanism.",
    "From humble beginnings, Flyers Charitable Trust has grown into a respected organization dedicated to life education and holistic human development. Our journey reflects our commitment to making a meaningful difference in the lives of the underprivileged and marginalized communities."
)

# Update Mission to Our Team
content = content.replace(
    '<h2 class="elementor-heading-title elementor-size-default">MISSION\n</h2>',
    '<h2 class="elementor-heading-title elementor-size-default">OUR TEAM\n</h2>'
)

content = content.replace(
    "The organization's goal is to identify, plan, design, implement, manage, monitor, and help people have healthy social lives in harmony with one another in a safe environment.",
    "Our team comprises dedicated professionals, volunteers, and passionate individuals who share a common vision of creating positive change. Together, we work tirelessly to implement programs that foster mental health, emotional well-being, and social harmony in our communities."
)

# Update Objectives to Our Values
content = content.replace(
    '<h2 class="elementor-heading-title elementor-size-default">OBJECTIVES</h2>',
    '<h2 class="elementor-heading-title elementor-size-default">OUR VALUES</h2>'
)

content = content.replace(
    '<h2 class="elementor-heading-title elementor-size-default">Because Every Life Deserves Care</h2>',
    '<h2 class="elementor-heading-title elementor-size-default">Guided by Compassion and Integrity</h2>'
)

content = content.replace(
    "<p>The organization's goal is to help the underprivileged get equal and genuine personal development in society, as well as equal opportunities to develop robust and long-lasting programs that will enhance their quality of life and positively impact the community's weaker segments.</p>",
    "<p>At Flyers Charitable Trust, our values are rooted in compassion, integrity, and transparency. We believe in empowering individuals through life education and creating sustainable programs that foster long-term positive change. Our team is committed to serving with dedication, ensuring that every initiative reflects our core principles of respect, inclusivity, and social responsibility.</p>"
)

# Update feature lists
content = content.replace(
    '<span class="elementor-icon-list-text">Life Education Focus</span>',
    '<span class="elementor-icon-list-text">Experienced Leadership</span>'
)

content = content.replace(
    '<span class="elementor-icon-list-text">Compassionate Service</span>',
    '<span class="elementor-icon-list-text">Dedicated Volunteers</span>'
)

content = content.replace(
    '<span class="elementor-icon-list-text">Community Focused</span>',
    '<span class="elementor-icon-list-text">Collaborative Approach</span>'
)

content = content.replace(
    '<span class="elementor-icon-list-text">Transparency &amp; Trust</span>',
    '<span class="elementor-icon-list-text">Professional Expertise</span>'
)

content = content.replace(
    '<span class="elementor-icon-list-text">Proven Dedication</span>',
    '<span class="elementor-icon-list-text">Passionate Service</span>'
)

content = content.replace(
    '<span class="elementor-icon-list-text">Inclusive Impact</span>',
    '<span class="elementor-icon-list-text">Results-Driven Goals</span>'
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated Our-Story-Team.html successfully!")
