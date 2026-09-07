#Number to Frequency Dictionary

numbers = [10, 20, 10, 30, 20, 10, 40, 30]
dictionary = {}
for num in numbers:
    if num in dictionary:
        dictionary[num] += 1
    else:
        dictionary[num] = 1

print(dictionary)