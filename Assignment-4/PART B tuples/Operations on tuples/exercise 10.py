numbers = (10, 20, 30)

try:
    numbers[0] = 100
except TypeError as e:
    print(type(e).__name__)

# Output:
# TypeError
