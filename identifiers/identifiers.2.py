import keyword

identifiers = [
    "2value",
    "value_2",
    "_hidden",
    "class",
    "my-var",
    "MyClass",
    "total$"
]

for name in identifiers:
    if not name.isidentifier():
        print(name, "-> Invalid Identifier")
    elif keyword.iskeyword(name):
        print(name, "-> Invalid Identifier (Python Keyword)")
    else:
        print(name, "-> Valid Identifier")
