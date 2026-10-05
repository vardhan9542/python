counter = 0

def show_local():
    counter = 10
    print("Local counter:", counter)

show_local()
print("Global counter:", counter)


# Output:
# Local counter: 10
# Global counter: 0