import re

def clean_text(html):
    text = re.sub(r"<[^>]+>", "", html)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

html = "<p>Hello   <b>World</b></p>\n\nThis is   Python."

print(clean_text(html))


# Output:
# Hello World This is Python.