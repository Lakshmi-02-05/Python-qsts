#Find Duplicate Elements

numbers = [1, 2, 3, 2, 4, 5, 1, 6, 3]
duplicate = []
for num in numbers:
    if numbers.count(num) > 1 and num not in duplicate:
        duplicate.append(num)

print("Duplicate Values: ", duplicate)