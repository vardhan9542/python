s = input("Enter a string: ")

counts = {}

for ch in s:
    counts[ch] = counts.get(ch, 0) + 1

print("Duplicate characters:")

for ch in counts:
    if counts[ch] > 1:
        print(ch, ":", counts[ch])


# Output:
# Enter a string: programming
# Duplicate characters:
# r : 2
# g : 2
# m : 2