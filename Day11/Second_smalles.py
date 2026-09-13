#Find the second smallest number

arr = [8, 3, 5, 3, 1, 8, 2, 1]
sm = arr[0]
sec_sm = arr [0]
for num in arr:
    if num < sm:
        sec_sm = sm 
        sm = num
    elif num < sec_sm and num != sm:
        sec_sm = num
print(f"The second smallest number is: {sec_sm}")