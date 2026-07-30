#Y.Mukhesh
#commands
import sys
if len(sys.argv) != 3:
    print("Usage: python sum_args.py <num1> <num2>")
else:
    # Convert arguments to integers
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])

    # Print the sum
    print("Sum =", num1 + num2)
