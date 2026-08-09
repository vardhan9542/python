list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(list1 == list2)
print(list1 is list2)
print(list1 is list3)

print(id(list1))
print(id(list2))
print(id(list3))
"""
Output:
True
False
True
140234567890112
140234567890304
140234567890112
"""
