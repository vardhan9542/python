set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)

# Output:
# Union: {1, 2, 3, 4, 5, 6}
# Intersection: {3, 4}
# Difference: {1, 2}
# Symmetric Difference: {1, 2, 5, 6}