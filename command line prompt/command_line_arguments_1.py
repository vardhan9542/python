import sys

if len(sys.argv) < 2:
    print("Usage: python Command_Line_Arguments_1.py <name>")
else:
    name = sys.argv[1]
    print("Hello,", name + "!")
