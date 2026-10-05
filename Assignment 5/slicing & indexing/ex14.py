s = input("Enter a string: ")
ch = input("Enter character: ")

first = s.find(ch)
last = s.rfind(ch)

print("First occurrence:", first)
print("Last occurrence:", last)

# Output:
# Enter a string: banana
# Enter character: a
# First occurrence: 1
# Last occurrence: 5