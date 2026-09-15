# Find duplicate elements

arr = [1, 2, 3, 2, 4, 5, 1, 6, 3]
duplicate_ele = set ()
for num in arr:
    if arr.count(num) > 1:
        duplicate_ele.add(num)
print("The duplicate elements in the array are:", duplicate_ele)