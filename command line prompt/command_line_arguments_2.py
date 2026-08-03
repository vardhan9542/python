# Import the sys module
import sys

# Check if exactly two numbers are provided
if len(sys.argv) != 3:
    print("Usage: python Command_Line_Arguments_2.py <num1> <num2>")
else:
    # Convert command-line arguments to integers
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])

    # Print the sum
    print("Sum =", num1 + num2)
