#Find the Largest Number in a List

list = [23,45,45,24,76,8]
# print(max(list))

# OR

largest = list[0]
for num in list:
    if num > largest:
        largest = num

print("Largrest is: ",largest)
