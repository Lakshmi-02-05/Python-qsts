#Find the second largest number.

numbers = [10, 25, 7, 43, 18, 43, 2]

largest = numbers[0]
sec_largest = numbers[1]

# if sec_largest > largest:
#     largest, sec_largest = sec_largest, largest
for num in numbers:
    if num > largest:
        sec_largest = largest
        largest = num
    elif num > sec_largest and num != largest:
        sec_largest = num

print("Largest:", largest)
print("Second largest:", sec_largest)