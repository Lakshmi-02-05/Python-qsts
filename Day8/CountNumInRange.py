#Count Numbers in a Range

numbers = [5, 12, 18, 3, 25, 9, 30, 14]
minimum = 10
maximum = 20
count = 0
for num in numbers:
    if minimum <= num >= maximum:
        count += 1
print("The count of numbers in the range", minimum, "to", maximum, "is:", count)