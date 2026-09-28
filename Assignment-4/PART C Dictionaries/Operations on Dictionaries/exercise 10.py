prices = {
    "Laptop": 60000,
    "Phone": 30000,
    "Tablet": 20000,
    "Watch": 10000
}

highest = max(prices, key=prices.get)
lowest = min(prices, key=prices.get)

print("Highest:", highest, prices[highest])
print("Lowest:", lowest, prices[lowest])

# Output:
# Highest: Laptop 60000
# Lowest: Watch 10000
