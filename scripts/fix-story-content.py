import codecs

file_path = r"c:\Users\smnk2\Downloads\flyers\Our-Story-Team.html"

# Read with explicit UTF-8-sig encoding to handle BOM if present
with codecs.open(file_path, "r", encoding="utf-8-sig") as f:
    content = f.read()

# Track changes
changes_made = 0

# Replace text 1
old1 = "The organization's vision is to create excellent people and live a truly joyful life that is full of humanism."
new1 = "From humble beginnings, Flyers Charitable Trust has grown into a respected organization dedicated to life education and holistic human development. Our journey reflects our commitment to making a meaningful difference in the lives of the underprivileged and marginalized communities."
if old1 in content:
    content = content.replace(old1, new1)
    changes_made += 1
    print(f"✓ Updated Vision text")
else:
    print(f"✗ Could not find Vision text")

# Replace text 2
old2 = "The organization's goal is to identify, plan, design, implement, manage, monitor, and help people have healthy social lives in harmony with one another in a safe environment."
new2 = "Our team comprises dedicated professionals, volunteers, and passionate individuals who share a common vision of creating positive change. Together, we work tirelessly to implement programs that foster mental health, emotional well-being, and social harmony in our communities."
if old2 in content:
    content = content.replace(old2, new2)
    changes_made += 1
    print(f"✓ Updated Mission text")
else:
    print(f"✗ Could not find Mission text")

# Replace text 3
old3 = "The organization's goal is to help the underprivileged get equal and genuine personal development in society, as well as equal opportunities to develop robust and long-lasting programs that will enhance their quality of life and positively impact the community's weaker segments."
new3 = "At Flyers Charitable Trust, our values are rooted in compassion, integrity, and transparency. We believe in empowering individuals through life education and creating sustainable programs that foster long-term positive change. Our team is committed to serving with dedication, ensuring that every initiative reflects our core principles of respect, inclusivity, and social responsibility."
if old3 in content:
    content = content.replace(old3, new3)
    changes_made += 1
    print(f"✓ Updated Objectives text")
else:
    print(f"✗ Could not find Objectives text")

# Write back
with codecs.open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"\nTotal changes made: {changes_made}/3")
print("File updated successfully!")
