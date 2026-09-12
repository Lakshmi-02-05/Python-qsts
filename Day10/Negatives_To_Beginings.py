#Move all negative numbers to the beginning

arr = [4, -2, 7, -5, 0, -1, 3]
negative = [x for x in arr if x < 0]
non_negative = [x for x in arr if x >= 0]
result = negative + non_negative
print("Array after moving negatives to the beginning:", result)