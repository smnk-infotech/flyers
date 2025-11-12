#!/usr/bin/env python
import os

for filename in os.listdir("."): 
    if filename.endswith(".html"):
        with open(filename, "r") as f:
            content = f.read()
        
        content = content.replace("href=\"css/", "href=\"/css/")
        content = content.replace("src=\"images/", "src=\"/images/")
        content = content.replace("src=\"js/", "src=\"/js/")
        content = content.replace("href=\"index.html\"", "href=\"/index.html\"")
        content = content.replace("href=\"About-Us.html\"", "href=\"/About-Us.html\"")
        content = content.replace("href=\"Services.html\"", "href=\"/Services.html\"")
        content = content.replace("href=\"Donation.html\"", "href=\"/Donation.html\"")
        content = content.replace("href=\"Gallery.html\"", "href=\"/Gallery.html\"")
        content = content.replace("href=\"Contact-Us.html\"", "href=\"/Contact-Us.html\"")

        with open(filename, "w") as f:
            f.write(content)
