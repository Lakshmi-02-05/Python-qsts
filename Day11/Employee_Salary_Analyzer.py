# Employee Salary Analyzer 
# 1. The highest-paid employee
# 2. The lowest-paid employee
# 3. The average salary
# 4. Employees earning more than the average salary
# 5. Total salary expenditure

employees = {
    "Asha": 35000,
    "Rahul": 42000,
    "Priya": 55000,
    "Arjun": 28000,
    "Sneha": 48000
}

highest_paid = max(employees, key = employees.get)
print(f"Highest paid employee: {highest_paid} with salary {employees[highest_paid]}")

lowest_paid = min(employees, key = employees.get)
print(f"Lowest paid employee: {lowest_paid} with salary {employees[lowest_paid]}")

avg = sum(employees.values()) / len(employees)
print(f"Average salary: {avg}")

more_than_avg = [name for name, salary in employees.items() if salary > avg]
print(f"Employees earning more than the average salary: {', '.join(more_than_avg)}")

total_expenditure = sum(employees.values())
print(f"Total salary expenditure: {total_expenditure}")