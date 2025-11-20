import codecs

file_path = r"c:\Users\smnk2\Downloads\flyers\Our-Story-Team.html"

# Read file
with codecs.open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Extract the exact original strings from the file
idx1 = content.find("The organization's vision")
if idx1 >= 0:
    old1 = content[idx1:idx1+115]  # Extract exact string
    print(f"Found text 1: {repr(old1[:50])}")
else:
    print("Could not find text 1")
    old1 = None

idx2 = content.find("The organization's goal is to identify")
if idx2 >= 0:
    old2 = content[idx2:idx2+165]  # Extract exact string
    print(f"Found text 2: {repr(old2[:50])}")
else:
    print("Could not find text 2")
    old2 = None

idx3 = content.find("The organization's goal is to help")
if idx3 >= 0:
    # Find the end of the sentence
    end_idx = content.find(".</p>", idx3) + 1
    if end_idx > idx3:
        old3 = content[idx3:end_idx]
        print(f"Found text 3 ({len(old3)} chars): {repr(old3[:50])}")
    else:
        old3 = None
else:
    print("Could not find text 3")
    old3 = None

# Perform replacements
changes_made = 0

if old1:
    new1 = "From humble beginnings, Flyers Charitable Trust has grown into a respected organization dedicated to life education and holistic human development. Our journey reflects our commitment to making a meaningful difference in the lives of the underprivileged and marginalized communities."
    content = content.replace(old1, new1)
    changes_made += 1
    print("✓ Replaced text 1")

if old2:
    new2 = "Our team comprises dedicated professionals, volunteers, and passionate individuals who share a common vision of creating positive change. Together, we work tirelessly to implement programs that foster mental health, emotional well-being, and social harmony in our communities."
    content = content.replace(old2, new2)
    changes_made += 1
    print("✓ Replaced text 2")

if old3:
    new3 = "At Flyers Charitable Trust, our values are rooted in compassion, integrity, and transparency. We believe in empowering individuals through life education and creating sustainable programs that foster long-term positive change. Our team is committed to serving with dedication, ensuring that every initiative reflects our core principles of respect, inclusivity, and social responsibility."
    content = content.replace(old3, new3)
    changes_made += 1
    print("✓ Replaced text 3")

# Write back
with codecs.open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"\n✅ Total changes made: {changes_made}")
print("File updated successfully!")
