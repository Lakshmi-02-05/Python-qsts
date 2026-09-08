#Move All Zeros to the End

numbers = [0, 5, 0, 3, 8, 0, 2, 1]
non_zeros = [x for x in numbers if x != 0]
zeros = [x for x in numbers if x == 0]
result = non_zeros + zeros
print(result)