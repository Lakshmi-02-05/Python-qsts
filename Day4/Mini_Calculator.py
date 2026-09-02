#Q8 — Mini Calculator

def add(a,b):
    return f"Addition of {a} and {b} is: {a + b}"

def sub(a,b):
    return f"Subtraction os {a} and {b} is: {a - b}"

def mul(a,b):
    return f"Multiplation of {a} and {b} is: {a * b}"

def div(a,b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return f"Division of {a} and {b} is: {a / b}"

num1 = int(input("Enter your 1st num: "))
num2 = int(input("Enter your 2nd num: "))
operation = input("Choose your operation (+, -, X, %): ")

if operation == "+":
    print(add(num1,num2))

elif operation == "-":
    print(sub(num1,num2))

elif operation == "X":
    print(mul(num1,num2))

elif operation == "%":
    print(div(num1,num2))
