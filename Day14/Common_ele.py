# Find elements that appear in both lists

a = [1, 2, 2, 3, 4, 5, 5]
b = [2, 3, 3, 5, 6, 7]

common = [x for x in set(a)if x in set(b)]
print(common)