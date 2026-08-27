#Take a number from the user and print whether it is: Positive,Negative or Zero

num = int(input("Enter any number: "))

if(num < 0):
    print(num,"is Negative number")
elif(num > 0):
    print(num,"is Positive number")
else:
    print(num,"is Zero")
