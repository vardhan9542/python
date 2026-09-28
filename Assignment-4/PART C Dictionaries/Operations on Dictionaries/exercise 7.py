student = {"name": "Ravi", "age": 20, "course": "Python"}

student.pop("age")

print(student)
print(student.get("phone", "Key not found"))

# Output:
# {'name': 'Ravi', 'course': 'Python'}
# Key not found