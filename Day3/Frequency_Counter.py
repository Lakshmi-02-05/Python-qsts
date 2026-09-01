# Find how many times each number occurs.

numbers = [1, 2, 2, 3, 1, 4, 2, 3, 4, 4]
freq = {}

for num in numbers:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(freq)