num = int(input("Enter a number: "))

original = num
reverse = 0
temp = abs(num)

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

if abs(original) == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")

# Output:
# Enter a number: 121
# Palindrome
