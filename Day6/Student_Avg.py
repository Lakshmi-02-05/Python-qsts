#Student Average: Calculate the average marks of each student in a dictionary

students = {
    "Rahul": [80, 75, 90],
    "Priya": [95, 88, 92],
    "Aman": [70, 65, 72],
    "Sneha": [85, 90, 88]
}

average = {}
for student, marks in students.items():
    avg = sum(marks) / len(marks)
    average[student] = avg
print(average)

highest_stu = max(average, key=average.get)
print("Highest:",highest_stu, ":" ,average[highest_stu])