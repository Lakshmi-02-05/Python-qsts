# Count the frequency of each number

numbers = [2, 3, 2, 5, 3, 2, 4, 5]
freq = {}
for num in numbers:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(freq)