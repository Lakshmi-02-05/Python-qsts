#Find the first repeated element

arr = [5, 3, 1, 4, 3, 5, 2]
seen = []
for num in arr:
    if num in seen:
        print("First repeated element:", num)
        break
    seen.append(num)
    