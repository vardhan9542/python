import re

pattern = r"^[A-Za-z_][A-Za-z0-9_]*$"

values = ["_count2", "2fast", "total_sum"]

for value in values:
    print(value, bool(re.fullmatch(pattern, value)))

# Output:
# _count2 True
# 2fast False
# total_sum True