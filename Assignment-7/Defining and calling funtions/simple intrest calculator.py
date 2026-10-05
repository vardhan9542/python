def simple_interest(principal, rate, time):
    """Calculate simple interest."""
    return (principal * rate * time) / 100

principal = float(input("Enter principal: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time: "))

si = simple_interest(principal, rate, time)

print("Simple Interest:", si)

# Output:
# Enter principal: 10000
# Enter rate: 5
# Enter time: 2