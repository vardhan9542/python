num = int(input("Enter a number: "))

num = abs(num)

if num == 0:
    digit_sum = 0
    count = 1
else:
    digit_sum = 0
    count = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        digit_sum += digit
        count += 1
        temp //= 10

average = digit_sum / count

print("Sum of digits:", digit_sum)
print("Average of digits:", average)
