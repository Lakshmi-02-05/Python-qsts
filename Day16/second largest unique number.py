# second largest unique number

numbers = [12, 5, 8, 12, 20, 8, 17, 20]
number = list(set(numbers))
number.sort(reverse=True)

print(f"The second largest unique number is: {number[1]}")
