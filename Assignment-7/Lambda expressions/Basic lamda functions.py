square = lambda x: x * x
even = lambda x: x % 2 == 0
larger = lambda a, b: a if a > b else b

print(square(5))
print(even(8))
print(larger(10, 20))