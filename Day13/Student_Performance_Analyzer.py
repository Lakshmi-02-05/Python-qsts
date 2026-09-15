# Student Performance Analyzer

students = {
    "Rahul": {"math": 80, "python": 75, "sql": 90},
    "Priya": {"math": 95, "python": 92, "sql": 96},
    "Arjun": {"math": 60, "python": 70, "sql": 65},
    "Sneha": {"math": 88, "python": 85, "sql": 90}
}

avg1 = []

# Each student's average marks
for student, marks in students.items():
    avg = sum(marks.values()) / len(marks)
    print(f"{student}: {avg:.2f}")
    avg1.append(avg)

# Topper
topper_avg = max(avg1)
topper_index = avg1.index(topper_avg)
topper_student = list(students.keys())[topper_index]

print(f"\nTopper is {topper_student} with avg marks: {topper_avg:.2f}")

# Lowest-performing student
lowest_avg = min(avg1)
lowest_index = avg1.index(lowest_avg)
lowest_student = list(students.keys())[lowest_index]

print(f"Lowest average marks is {lowest_student} with avg marks: {lowest_avg:.2f}")

# Highest-scoring student in Python
highest_python_score = max(
    students.items(),
    key=lambda x: x[1]["python"]
)

print(
    f"Highest scoring student in Python is "
    f"{highest_python_score[0]} with marks: "
    f"{highest_python_score[1]['python']}"
)

# Students whose average is 80 or above
distinction = [
    student
    for student, avg in zip(students.keys(), avg1)
    if avg >= 80
]

print(f"Students with distinction: {distinction}")