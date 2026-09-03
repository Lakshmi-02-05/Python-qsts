#Student Marks: combine dictionaries + functions.
#Create a function: It should return the name of the student with the highest marks.

students = {
    "Rahul": 85,
    "Priya": 92,
    "Aman": 76,
    "Sneha": 89,
    "Karan": 95
}

def find_topper(students):
    highest_marks = 0
    topper_name = ""
    for name,marks in students.items():
        if marks > highest_marks:
            highest_marks = marks
            topper_name = name
    return f"Topper: {topper_name} \nScore: {highest_marks}"

print(find_topper(students))