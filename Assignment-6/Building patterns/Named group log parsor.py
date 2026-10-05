import re

log = "2024-06-01 08:15:32 ERROR Disk full"

pattern = r"(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2}) (?P<level>\w+) (?P<message>.*)"

m = re.search(pattern, log)

print(m.group("date"))
print(m.group("time"))
print(m.group("level"))
print(m.group("message"))


# OPutput:
# 2024-06-01
# 08:15:32
# ERROR
# Disk full