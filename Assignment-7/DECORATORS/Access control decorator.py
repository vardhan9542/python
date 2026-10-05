from functools import wraps

is_logged_in = False

def require_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if is_logged_in:
            return func(*args, **kwargs)
        else:
            print("Access denied")

    return wrapper

@require_login
def dashboard():
    print("Welcome to dashboard")

dashboard()

is_logged_in = True

dashboard()

# Output:
# Access denied
# Welcome to dashboard