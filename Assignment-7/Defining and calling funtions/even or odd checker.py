def is_even(n):
    return n % 2 == 0

for i in range(5):
    n = int(input("Enter number: "))

    if is_even(n):
        print(n, "is Even")
        break
    else:
        print(n, "is Odd")
        break

# Output:
# Enter number: 7
# 7 is Odd