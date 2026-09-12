#Find the second most frequent element

arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
freq ={}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

max_freq = 0
sec_max_freq = 0
for key, value in freq.items():
    if value > max_freq:
        sec_max_freq = max_freq
        max_freq = value
    elif value > sec_max_freq and value != max_freq:
        sec_max_freq = value

print("Second most frequent element:", sec_max_freq)