def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

numbers = range(1, 51)

primes = list(filter(is_prime, numbers))

words = ["madam", "hello", "level", "python", "radar"]

palindromes = list(filter(lambda x: x == x[::-1], words))

print(primes)
print(palindromes)

# Output:
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
# ['madam', 'level', 'radar']