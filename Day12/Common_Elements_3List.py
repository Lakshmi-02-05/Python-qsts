#Find common elements in three lists

a = [1, 2, 3, 4, 5]
b = [2, 3, 5, 7]
c = [0, 2, 3, 5, 9]
common = [x for x in a if x in b and x in c]
print("Common Elements in the given three lists are:", common)