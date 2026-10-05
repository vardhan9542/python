import re

text = "1024 requests were served in 3 seconds"

m1 = re.match(r"\d", text)
m2 = re.search(r"served", text)
m3 = re.fullmatch(r"\d+", "12345")
m4 = re.fullmatch(r"\d+", "123a5")

print(m1.group())
print(m2.span())
print(m3.group())
print(m4)

# Output:
# 1
# (20, 26)
# 12345
# None