# Find the sum of even numbers

numbers = [12, 7, 4, 9, 16, 3, 10]
sum_even = 0
for num in numbers:
    if num % 2 == 0:
        sum_even = num + sum_even
print(sum_even)
