def greet(name):
    return "Hello " + name

f = greet

print(f("Ravi"))

def call_function(func, name):
    print(func(name))

call_function(greet, "Sita")

def create_function():
    def message():
        return "Function returned successfully"
    return message

new_function = create_function()

print(new_function())

# Output:
# Hello Ravi
# Hello Sita
# Function returned successfully