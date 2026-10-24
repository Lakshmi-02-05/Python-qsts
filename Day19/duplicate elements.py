# Find duplicate elements in a list

num = [1, 2, 3, 2, 4, 1, 5]
n1 = set()
duplicate = set()
for n in num:
    if n in n1:
        duplicate.add(n)
    else:
        n1.add(n)

print("Duplicate elements in the list are:", duplicate)

