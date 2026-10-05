import re

text = "I have a cat, a dog, a bird and another cat"

pattern = r"\b(cat|dog|bird)\b"

print(re.findall(pattern, text))

# Output:
# ['cat', 'dog', 'bird', 'cat']