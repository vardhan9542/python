def calculate_price(price, tax_rate=18, discount=0):
    tax = price * tax_rate / 100
    discount_amount = price * discount / 100
    return price + tax - discount_amount

print(calculate_price(1000))
print(calculate_price(1000, 10))
print(calculate_price(1000, 10, 5))

# Output:
# 1180.0
# 1100.0
# 1050.0