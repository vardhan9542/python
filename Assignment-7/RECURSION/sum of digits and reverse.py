def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)

def reverse_number(n, result=0):
    if n == 0:
        return result
    return reverse_number(n // 10, result * 10 + n % 10)

n = 12345

print("Sum:", sum_of_digits(n))
print("Reverse:", reverse_number(n))

# Output:
# Sum: 15
# Reverse: 54321