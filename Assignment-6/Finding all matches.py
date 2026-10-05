import re

text = "NASA and USA are working with ISRO on advanced TECHNOLOGY projects"

capital_words = re.findall(r"\b[A-Z]{2,}\b", text)

print(capital_words)

for match in re.finditer(r"\b\w{7,}\b", text):
    print(match.group(), match.start())

prices = "apples: $3.50, bananas: $1.20, mango: $4.75"
amounts = re.findall(r"\$\d+\.\d+", prices)

print(amounts)
print(len(amounts))

# Output:
# ['NASA', 'USA', 'ISRO', 'TECHNOLOGY']
# working 17
# advanced 38
# TECHNOLOGY 47
# projects 58
# ['$3.50', '$1.20', '$4.75']
# 3