grade = lambda marks: "Pass" if marks >= 40 else "Fail"

marks = [35, 45, 60, 28, 75, 39]

for mark in marks:
    print(mark, grade(mark))

# Output:
# 35 Fail
# 45 Pass
# 60 Pass
# 28 Fail
# 75 Pass
# 39 Fail