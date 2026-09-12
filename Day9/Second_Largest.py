#Find Second Largest Element in an Array

arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
largest = arr[0]
sec_largest = arr[1]

for num in arr:
    if num > largest:
        sec_largest = largest
        largest = num
    elif num > sec_largest and num != largest:
        sec_largest = num

print("Second largest:", sec_largest)

