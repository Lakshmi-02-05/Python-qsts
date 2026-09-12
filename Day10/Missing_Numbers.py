#Find the missing numbers & Numbers should be from 1 to n.

arr = [1, 2, 4, 6, 7]
n = 7
missing_num = []
for num in range(1, n + 1):
    if num not in arr:
        missing_num.append(num)
print("Missing numbers:", missing_num)