# longest consecutive sequence

arr = [100, 4, 200, 1, 3, 2]
arr_set = set(arr)
longest = 0
for num in arr_set:
    if num - 1 not in arr_set:
        current = num
        count = 1

    while current + 1 in arr_set:
        current += 1
        count += 1
    if count > longest:
        longest = count
print("The length of the longest consecutive sequence is:", longest)