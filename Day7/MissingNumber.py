#Find Missing Number

numbers = [1, 2, 3, 5, 6]
for n in range(1,len(numbers)):
    if n not in numbers:
        print(f"Missing number is: {n}")