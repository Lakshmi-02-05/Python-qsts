#Take three numbers from the user and find the largest number.

n1 = int(input("Enters your 1st number: "))
n2 = int(input("Enters your 2nd number: "))
n3 = int(input("Enters your 3rd number: "))

if(n1 > n2 and n1 > n3):
    print(n1,"is the largest number among the given 3 numbers")
elif(n2 > n1 and n2 > n3):
    print(n2,"is the largest number among the given 3 numbers")
else:
    print(n3,"is the largest number among the given 3 numbers")