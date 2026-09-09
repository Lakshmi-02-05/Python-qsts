#Compress Consecutive Duplicates

numbers = [1, 1, 2, 2, 2, 3, 3, 4, 1, 1]
compressed = []
for i in range(len(numbers)):
    if i == 0 or numbers[i] != numbers[i-1]:
        compressed.append(numbers[i])
print("Compressed list:", compressed)