year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

if month < 1 or month > 12:
    print("Invalid date")
else:
    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_days = 31
    elif month in [4, 6, 9, 11]:
        max_days = 30
    else:
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            max_days = 29
        else:
            max_days = 28

    if 1 <= day <= max_days:
        print("Valid date")
    else:
        print("Invalid date")

# Output:
# Enter year: 2026
# Enter month: 4
# Enter day: 5
# Valid date
