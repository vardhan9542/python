import re

log = """[2024-06-01 08:15:32] ERROR user=jsmith msg="Disk quota exceeded"
[2024-06-01 08:16:05] INFO user=agarcia msg="Login successful"
[2024-06-01 08:17:44] WARN user=jsmith msg="High memory usage"
"""

pattern = r'\[(?P<timestamp>.*?)\] (?P<level>\w+) user=(?P<user>\w+) msg="(?P<msg>.*?)"'

entries = []

for match in re.finditer(pattern, log):
    entries.append(match.groupdict())

print(entries)

error_count = len(re.findall(r"\] ERROR ", log))
warn_count = len(re.findall(r"\] WARN ", log))
info_count = len(re.findall(r"\] INFO ", log))

print("ERROR:", error_count)
print("WARN:", warn_count)
print("INFO:", info_count)

redacted = re.sub(r"user=\w+", "user=<hidden>", log)

print(redacted)

# Output:
# [{'timestamp': '2024-06-01 08:15:32', 'level': 'ERROR', 'user': 'jsmith', 'msg': 'Disk quota exceeded'}, {'timestamp': '2024-06-01 08:16:05', 'level': 'INFO', 'user': 'agarcia', 'msg': 'Login successful'}, {'timestamp': '2024-06-01 08:17:44', 'level': 'WARN', 'user': 'jsmith', 'msg': 'High memory usage'}]
# ERROR: 1
# WARN: 1
# INFO: 1
# [2024-06-01 08:15:32] ERROR user=<hidden> msg="Disk quota exceeded"
# [2024-06-01 08:16:05] INFO user=<hidden> msg="Login successful"
# [2024-06-01 08:17:44] WARN user=<hidden> msg="High memory usage"