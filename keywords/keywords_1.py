# Import the keyword module
import keyword

# Print the total number of keywords
print("Total number of keywords:", len(keyword.kwlist))

# Print the full list of keywords
print("List of keywords:")
for word in keyword.kwlist:
    print(word)
