import re

text = "Colors are #FFAA00, #000, #123ABC and #GGG"

pattern = r"#[0-9A-Fa-f]{3}(?:[0-9A-Fa-f]{3})?"

print(re.findall(pattern, text))

# Outptu:
# ['#FFAA00', '#000', '#123ABC']