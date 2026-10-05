def total_marks(*marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

print(total_marks(80, 90, 70))
print(total_marks(80, 90, 70, 60, 85))
print(total_marks(95))

# Output:
# (240, 80.0)
# (385, 77.0)
# (95, 95.0)