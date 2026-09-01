#Find the smallest number using a loop.

numbers = [45, 12, 78, 3, 56, 9]
# print(min(numbers))

smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest is: ",smallest)