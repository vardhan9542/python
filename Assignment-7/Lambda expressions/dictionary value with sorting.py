items = {
    "Laptop": 60000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Monitor": 12000
}

result = sorted(items.items(), key=lambda x: x[1])

print(result)

# Output:
# [('Mouse', 800), ('Keyboard', 1500), ('Monitor', 12000), ('Laptop', 60000)]