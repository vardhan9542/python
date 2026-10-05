s = input("Enter a sentence: ")

words = s.split()
result = []

for word in words:
    result.append(word[0].upper() + word[1:].lower())

print("Title Case:", " ".join(result))


# Output:
# Enter a sentence: python programming language
# Title Case: Python Programming Language