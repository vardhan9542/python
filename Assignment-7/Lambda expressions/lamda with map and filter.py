numbers = [1, 2, 3, 4, 5, 6]

cubes = list(map(lambda x: x ** 3, numbers))
divisible = list(filter(lambda x: x % 3 == 0, numbers))

print(cubes)
print(divisible)


# Output:
# [1, 8, 27, 64, 125, 216]
# [3, 6]