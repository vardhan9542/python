s = input("Enter a sentence: ")

words = s.split()
result = " ".join(words[::-1])

print("Reversed word order:", result)

# Output:
# Enter a sentence: Python is very easy
# Reversed word order: easy very is Python