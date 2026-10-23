# Create a Student class

# Create a class named Student with the following:
# - Attributes: name, marks
# - A constructor (__init__) to initialize these attributes.
# - A method called display() that prints the student's name and marks.
# - Create two student objects and call display() for both.


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


student1 = Student("Lakshmi", 90)
student2 = Student("Priya", 85)

student1.display()
student2.display()
