students = [
    ("Ravi", 78),
    ("Sita", 92),
    ("Amit", 65)
]

sorted_students = sorted(
    students,
    key=lambda s: s[1],
    reverse=True
)

print(sorted_students)

words = ["apple", "hi", "banana", "cat"]

print(sorted(words, key=lambda x: len(x)))


# Output:
# [('Sita', 92), ('Ravi', 78), ('Amit', 65)]
# ['hi', 'cat', 'apple', 'banana']