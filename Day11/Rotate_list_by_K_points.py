# Rotate a list to the right by k positions

arr = [1, 2, 3, 4, 5]
k = 2
k = k % len(arr)  # Handle cases where k is larger than the list length
arr = arr[-k:] + arr[:-k]
print(f"The rotated list is: {arr}")