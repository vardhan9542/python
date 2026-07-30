#N.Guna vardhan
#seperated by spaces
numbers = input("Enter numbers separated by spaces: ").split()
numbers = list(map(int, numbers))
print("Sum =", sum(numbers))

#output
#Enter numbers separated by spaces: 10 20 30 40 50
#Sum = 150
