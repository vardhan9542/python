# Take multiple numbers as input in one line
numbers = input("Enter numbers separated by spaces: ")

# Split the input and convert each value to an integer
num_list = list(map(int, numbers.split()))

# Find the sum
total = sum(num_list)

# Print the sum
print("Sum =", total)
