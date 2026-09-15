# Group numbers by even and odd

arr = [1, 2, 3, 4, 5, 6, 7, 8]

even_num = [num for num in arr if num % 2 == 0]
odd_num = [num for num in arr if num % 2 != 0]
print(f"Even Num: {even_num}")
print(f"Odd Num: {odd_num}")