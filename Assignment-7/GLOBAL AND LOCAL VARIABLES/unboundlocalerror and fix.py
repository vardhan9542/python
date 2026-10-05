counter = 10

def wrong():
    try:
        counter += 1
    except UnboundLocalError:
        print("UnboundLocalError occurred")

wrong()

def correct():
    global counter
    counter += 1
    print("Counter:", counter)

correct()

# Output:
# UnboundLocalError occurred
# Counter: 11