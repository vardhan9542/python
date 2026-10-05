import re

text = "Important dates are 01/06/2024, 15/08/2024 and 25/12/2024"

dates = re.findall(r"(\d{2})/(\d{2})/(\d{4})", text)

print(dates)

result = re.sub(
    r"(\d{2})/(\d{2})/(\d{4})",
    r"\3-\2-\1",
    text
)

print(result)

# Output:
# [('01', '06', '2024'), ('15', '08', '2024'), ('25', '12', '2024')]
# Important dates are 2024-06-01, 2024-08-15 and 2024-12-25