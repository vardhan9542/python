s = input("Enter a sentence: ")

words = s.split()
longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)

# Output:
# Enter a sentence: Python programming is interesting
# Longest word: programming