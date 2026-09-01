#Create a new list containing only unique values.

numbers = [1, 2, 2, 3, 4, 3, 5, 1, 6]
# my_set = set(numbers)
# print(my_set)

unique_num = []
for num in numbers:
    if num not in unique_num:
        unique_num.append(num)

print(unique_num)