#Take n from the user and calculate sum of n numbers

num = int(input("Enter any number: "))
i = 1
sum = 0

while i <= num:
    sum = sum + i
    i += 1

print("Sum: ", sum)