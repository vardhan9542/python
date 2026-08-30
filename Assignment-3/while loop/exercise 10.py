num = int(input("Enter an integer: "))

sign = -1 if num < 0 else 1
num = abs(num)

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

reverse *= sign

print("Reversed number:", reverse)

# Output:
# Enter an integer: 5467
# Reversed number: 7645
