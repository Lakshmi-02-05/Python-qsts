#Rotate a List

numbers = [1, 2, 3, 4, 5]
k = 2  # Number of positions to rotate
rotated = numbers[-k:] + numbers[:-k]
print(rotated)