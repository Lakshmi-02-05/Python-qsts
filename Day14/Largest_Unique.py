# Find the largest unique number

arr = [10, 5, 8, 10, 3, 8, 15, 15, 12]
largest = []
for num in arr:
    if arr.count(num) == 1:
        largest.append(num)
if largest:
    print(max(largest))
