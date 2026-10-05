from functools import reduce

employees = [
    {"name": "Ravi", "department": "IT", "salary": 40000},
    {"name": "Sita", "department": "HR", "salary": 35000},
    {"name": "Amit", "department": "IT", "salary": 50000},
    {"name": "Kiran", "department": "Sales", "salary": 45000}
]

it_employees = list(
    filter(lambda e: e["department"] == "IT", employees)
)

hiked = list(
    map(
        lambda e: {
            "name": e["name"],
            "department": e["department"],
            "salary": e["salary"] * 1.10
        },
        it_employees
    )
)

total = reduce(lambda a, b: a + b["salary"], hiked, 0)

print(hiked)
print("Total Salary:", total)

# Output:
# [{'name': 'Ravi', 'department': 'IT', 'salary': 44000.0}, {'name': 'Amit', 'department': 'IT', 'salary': 55000.00000000001}]
# Total Salary: 99000.0