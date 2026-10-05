s = input("Enter a string: ")

result = ""

for ch in s:
    if not ch.isspace():
        result += ch

print("Without whitespace:", result)

# Output:
# Enter a string: Hello World Python
# Without whitespace: HelloWorldPython