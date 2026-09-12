#Check if two lists contain the same elements

a = [1, 2, 3, 4]
b = [4, 3, 2, 1]
for n1 in a:
    if n1 not in b:
        print("Lists do not contain the same elements")
        break
else:
    print("Lists contain the same elements")
