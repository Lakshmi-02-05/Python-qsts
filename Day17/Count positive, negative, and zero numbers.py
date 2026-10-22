# Count positive, negative, and zero numbers

numbers = [10, -5, 0, 8, -2, 0, 7, -9]
pos_count = 0
neg_count = 0
zero_count = 0
for num in numbers: 
    if num > 0:
        pos_count += 1
    elif num < 0:
        neg_count += 1
    else:
        zero_count += 1
print("Positive numbers:", pos_count)
print("Negative numbers:", neg_count)
print("Zero numbers:", zero_count)
