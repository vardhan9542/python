import re

text = "Contact john@gmail.com or admin@yahoo.com"

result = re.sub(r"\b[\w.-]+@[\w.-]+\.\w+\b", "[EMAIL HIDDEN]", text)

print(result)

name = "Doe, John"
result2 = re.sub(r"(\w+),\s*(\w+)", r"\2 \1", name)

print(result2)

def double_number(match):
    return str(int(match.group()) * 2)

sentence = "I have 3 apples and 5 oranges"
result3 = re.sub(r"\d+", double_number, sentence)

print(result3)

text2 = "Wait!!! What??? Really!!!"
result4, count = re.subn(r"!{2,}", "!", text2)
result4, count = re.subn(r"\?{2,}", "?", result4)

print(result4)
print(count)

# Output:
# Contact [EMAIL HIDDEN] or [EMAIL HIDDEN]
# John Doe
# I have 6 apples and 10 oranges
# Wait! What? Really!
# 2