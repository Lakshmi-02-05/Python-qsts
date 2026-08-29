#Ask the user for a number and print all the factors of that number.

num = int(input("Enter an Number: "))

for n in range(1,num+1):
    if num % n == 0:
        print(n)