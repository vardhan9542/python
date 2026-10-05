def student_info(name, roll_no, branch):
    print("Name:", name)
    print("Roll No:", roll_no)
    print("Branch:", branch)

student_info("Ravi", 101, "CSE")

student_info(branch="CSE", name="Ravi", roll_no=101)

# Output:
# Name: Ravi
# Roll No: 101
# Branch: CSE
# Name: Ravi
# Roll No: 101
# Branch: CSE