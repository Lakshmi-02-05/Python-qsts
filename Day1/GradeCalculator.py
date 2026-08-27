#Take marks from the user and print the grade

marks = int(input("Enter you marks: "))

if(marks < 0 or marks > 100):
    print("Please enter a valid Marks")
elif(marks >= 90 and marks <=100):
    print("Congradulations, \nGrade: A")
elif(marks >=80 and marks <= 89):
    print("Well Done, \nGrade: B")
elif(marks >= 70 and marks <= 79):
    print("Doing Great, \nGrade: C")
elif(marks >= 60 and marks <= 69):
    print("Ahh, No worries you can do better dear \nGrade: D")
else:
    print("You can rock in future my dear \nGrade: F")
