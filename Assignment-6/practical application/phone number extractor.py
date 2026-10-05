import re

text = "Call 555-123-4567 or (555) 123-4567 or 555.123.4567"

pattern = r"(?:\(\d{3}\)|\d{3})[-.\s]\d{3}[-.]\d{4}"

numbers = re.findall(pattern, text)

for number in numbers:
    normalized = re.sub(r"\D", "", number)
    normalized = re.sub(r"(\d{3})(\d{3})(\d{4})", r"\1-\2-\3", normalized)
    print(normalized)

# Output:
# 555-123-4567
# 555-123-4567
# 555-123-4567