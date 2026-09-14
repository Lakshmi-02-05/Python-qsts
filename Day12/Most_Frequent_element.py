# Find the most frequent element

arr = [4, 2, 4, 3, 2, 4, 5, 3, 4]
freq_arr ={}
for num in arr:
    if num in freq_arr:
        freq_arr[num] += 1
    else:
        freq_arr[num] = 1

most_frequent = max(freq_arr, key=freq_arr.get)
print(f"The most frequent element is: {most_frequent} with frequency {freq_arr[most_frequent]}")


