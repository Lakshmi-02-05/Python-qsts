

numbers = [2, 4, 7, 9, 11, 15, 17, 20]
for num in numbers:
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num, "is a prime number.")