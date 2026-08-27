#Take an integer from the user and determine whether it is even or odd.

num = int(input("Please enter a number: "))
if(num % 2 == 0):
    print(num,"is an Even Number")
else:
    print(num,"is an Odd Number")