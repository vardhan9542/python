def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

while True:
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        c = float(input("Enter Celsius: "))
        print("Fahrenheit:", celsius_to_fahrenheit(c))

    elif choice == "2":
        f = float(input("Enter Fahrenheit: "))
        print("Celsius:", fahrenheit_to_celsius(f))

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice")


# Output:
# 1. Celsius to Fahrenheit
# 2. Fahrenheit to Celsius
# 3. Exit
# Enter choice: 1
# Enter Celsius: 25
# Fahrenheit: 77.0
# 1. Celsius to Fahrenheit
# 2. Fahrenheit to Celsius
# 3. Exit
# Enter choice: 3
# Exiting...