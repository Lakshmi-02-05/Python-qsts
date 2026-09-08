#Two Lists: Common + Unique

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common =[x for x in list1 if x in list2]
unique =list(set(list1) ^ set(list2))
print("Common elements:", common)
print("Unique elements:", unique)