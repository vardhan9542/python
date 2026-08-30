a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b:
    if a >= c:
        largest = a
    else:
        largest = c
else:
    if b >= c:
        largest = b
    else:
        largest = c

print("Largest number:", largest)

# Outpput:
# Enter first number: 45
# Enter second number: 56
# Enter third number: 22 
# Largest number: 56.0
