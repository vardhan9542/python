def order_summary(customer, *items, discount=0, **extra):
    print("Customer:", customer)
    print("Items:")

    for item in items:
        print("-", item)

    print("Discount:", discount, "%")

    for key, value in extra.items():
        print(key + ":", value)

order_summary(
    "Meera",
    "Laptop",
    "Mouse",
    discount=10,
    delivery_address="Hyderabad",
    gift_wrap=True
)

# Output:
# Customer: Meera
# Items:
# - Laptop
# - Mouse
# Discount: 10 %
# delivery_address: Hyderabad
# gift_wrap: True