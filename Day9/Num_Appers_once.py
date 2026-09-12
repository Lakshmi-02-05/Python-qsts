#Find numbers that appear exactly once

arr = [1, 2, 2, 3, 4, 4, 5, 6, 6]
new_arr = []
for num in arr:
    if arr.count(num) == 1:
        new_arr.append(num)
print(str(new_arr)[1:-1], "appears exactly once")