# Find the second-largest distinct number in an array

t = [10, 5, 20, 20, 8]
unique_num = list(set(t))
unique_num.sort()
second_largest = unique_num[-2]
print("The second-largest distinct number is:", second_largest)