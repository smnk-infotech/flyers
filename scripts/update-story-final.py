import codecs

file_path = r"c:\Users\smnk2\Downloads\flyers\Our-Story-Team.html"

# Read file
with codecs.open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Use the correct Unicode character for right single quotation mark
apos = chr(0x2019)

# Define replacements
replacements = [
    (
        f"The organization{apos}s vision is to create excellent people and live a truly joyful life that is full of humanism.",
        "From humble beginnings, Flyers Charitable Trust has grown into a respected organization dedicated to life education and holistic human development. Our journey reflects our commitment to making a meaningful difference in the lives of the underprivileged and marginalized communities."
    ),
    (
        f"The organization{apos}s goal is to identify, plan, design, implement, manage, monitor, and help people have healthy social lives in harmony with one another in a safe environment.",
        "Our team comprises dedicated professionals, volunteers, and passionate individuals who share a common vision of creating positive change. Together, we work tirelessly to implement programs that foster mental health, emotional well-being, and social harmony in our communities."
    ),
    (
        f"The organization{apos}s goal is to help the underprivileged get equal and genuine personal development in society, as well as equal opportunities to develop robust and long-lasting programs that will enhance their quality of life and positively impact the community{apos}s weaker segments.",
        "At Flyers Charitable Trust, our values are rooted in compassion, integrity, and transparency. We believe in empowering individuals through life education and creating sustainable programs that foster long-term positive change. Our team is committed to serving with dedication, ensuring that every initiative reflects our core principles of respect, inclusivity, and social responsibility."
    )
]

# Perform replacements
changes_made = 0
for old_text, new_text in replacements:
    if old_text in content:
        content = content.replace(old_text, new_text)
        changes_made += 1
        print(f"✓ Replaced: {old_text[:50]}...")
    else:
        print(f"✗ Not found: {old_text[:50]}...")

# Write back
with codecs.open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"\n✅ Total changes made: {changes_made}/3")
print("File updated successfully!")
