import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print("Execution time:", end - start)

        return result

    return wrapper

@timer
def calculate():
    total = 0

    for i in range(1000000):
        total += i

    return total

print("Result:", calculate())

# Output:
# Result: 499999500000
# Execution time: 0.0...