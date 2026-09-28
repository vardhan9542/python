numbers = [10, -5, 20, -8, 30, -2]

result = [0 if x < 0 else x for x in numbers]

print(result)


# Output:
# [10, 0, 20, 0, 30, 0]
