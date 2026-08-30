start = int(input("Enter lower limit: "))
end = int(input("Enter upper limit: "))

print("Prime numbers:")

for num in range(start, end + 1):
    if num < 2:
        continue

    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")
