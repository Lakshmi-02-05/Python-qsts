#Ask the user for a number and count how many times it appears.

numbers = [2, 5, 2, 8, 2, 9, 5, 2]
n = int(input("Enter an number: "))

for num in numbers:
    count = numbers.count(n)

print(count)

