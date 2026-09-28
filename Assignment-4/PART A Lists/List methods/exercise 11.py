numbers = [30, 10, 20]

numbers.append(40)
print("append:", numbers)

numbers.insert(1, 15)
print("insert:", numbers)

numbers.extend([50, 60])
print("extend:", numbers)

numbers.remove(15)
print("remove:", numbers)

numbers.pop()
print("pop:", numbers)

numbers.sort()
print("sort:", numbers)

numbers.reverse()
print("reverse:", numbers)

print("count:", numbers.count(30))
print("index:", numbers.index(30))

# Output:
# append: [30, 10, 20, 40]
# insert: [30, 15, 10, 20, 40]
# extend: [30, 15, 10, 20, 40, 50, 60]
# remove: [30, 10, 20, 40, 50, 60]
# pop: [30, 10, 20, 40, 50]
# sort: [10, 20, 30, 40, 50]
# reverse: [50, 40, 30, 20, 10]
# count: 1
# index: 2
