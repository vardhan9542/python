import re

def is_valid_email(s):
    pattern = r"^[\w.]+@[\w.]+\.[A-Za-z]{2,6}$"
    return bool(re.fullmatch(pattern, s))

emails = [
    "john@gmail.com",
    "alice.smith@yahoo.com",
    "user123@domain.in",
    "test@example.org",
    "a@b.c",
    "no-at-sign.com",
    "user@domain",
    "user@.com"
]

for email in emails:
    print(email, is_valid_email(email))

# Output:
# john@gmail.com True
# alice.smith@yahoo.com True
# user123@domain.in True
# test@example.org True
# a@b.c False
# no-at-sign.com False
# user@domain False
# user@.com False