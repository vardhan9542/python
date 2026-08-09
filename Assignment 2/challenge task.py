username = "admin"
password = "python123"

u = input("Enter Username: ")
p = input("Enter Password: ")

login_success = (u == username) and (p == password)

print("Login Success:", login_success)
"""
Output:
Enter Username: admin
Enter Password: python123
Login Success: True"""
