#Separate Positive and Negative Numbers
#Bonus: Put 0 into a third list.

numbers = [-5, 10, -2, 8, -9, 0, 15, -1]
p_num = []
n_num = []
n = []

for num in numbers:
    if num == 0:
        n.append(num)
    elif num > 0:
        p_num.append(num)
    else:
        n_num.append(num)

print("Positive Numbers: ", p_num)
print("Negative Numbers: ", n_num)
print("Hey heres one neither postive nor negative but Zero:", n)