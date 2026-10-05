s = input("Enter a string: ")

reverse1 = ""
for ch in s:
    reverse1 = ch + reverse1

reverse2 = s[::-1]

print("Without slicing:", reverse1)
print("With slicing:", reverse2)

# Output:
# Enter a string: Python
# Without slicing: nohtyP
# With slicing: nohtyP