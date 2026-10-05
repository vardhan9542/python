from functools import reduce

def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

temperatures = [0, 10, 20, 30, 40]

fahrenheit = list(map(celsius_to_fahrenheit, temperatures))

words = ["python", "java", "django"]

upper_words = list(map(str.upper, words))

print(fahrenheit)
print(upper_words)

# Output:
# [32.0, 50.0, 68.0, 86.0, 104.0]
# ['PYTHON', 'JAVA', 'DJANGO']