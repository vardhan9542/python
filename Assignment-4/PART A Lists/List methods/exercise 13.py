numbers = [25, 10, 45, 5, 30]

maximum = numbers[0]
minimum = numbers[0]
total = 0

for number in numbers:
    if number > maximum:
        maximum = number
    if number < minimum:
        minimum = number
    total += number

print("Maximum:", maximum)
print("Minimum:", minimum)
print("Sum:", total)

# Output:
# Maximum: 45
# Minimum: 5
# Sum: 115
