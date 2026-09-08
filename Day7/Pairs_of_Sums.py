#Find Pairs With a Given Sum

numbers = [2, 4, 3, 7, 5, 8, 1]
target = 9

for num in numbers:
    n = target - num
    if n in numbers and n != num:
        print(f"Pair found: ({num}, {n})")