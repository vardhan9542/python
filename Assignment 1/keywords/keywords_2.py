# Import the keyword module
import keyword

# Get input from the user
word = input("Enter a word: ")

# Check whether the word is a Python keyword
if keyword.iskeyword(word):
    print(word, "is a Python keyword.")
else:
    print(word, "is not a Python keyword.")
