# Mini Student Analyzer

students = {
    "Asha": [80, 90, 70],
    "Rahul": [65, 75, 70],
    "Priya": [95, 90, 100],
    "Sneha": [85, 80, 90]
}

avg = {}
for student, marks in students.items():
    avg[student] = sum(marks) / len(marks)
    print(f"{student}'s average marks: {avg[student]}")
    topper = max(students, key=lambda x: sum(students[x]) / len(students[x]))
   
print(f"The topper is {topper} with average marks: {topper}")