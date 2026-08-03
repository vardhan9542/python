# (a) Swapping using a temporary variable
a = 10
b = 20

print("Before swapping (using temporary variable):")
print("a =", a)
print("b =", b)

temp = a
a = b
b = temp

print("After swapping:")
print("a =", a)
print("b =", b)

# (b) Swapping using tuple unpacking
a = 10
b = 20

print("\nBefore swapping (using tuple unpacking):")
print("a =", a)
print("b =", b)

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)

#Before swapping (using temporary variable):
a = 10
#b = 20
#After swapping:
#a = 20
b = 10

#Before swapping (using tuple unpacking):
#a = 10
#b = 20
#After swapping:
#a = 20
b = 10
