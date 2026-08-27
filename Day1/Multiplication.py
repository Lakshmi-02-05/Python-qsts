#Take a number and print its multiplication table from 1 to 10.

num = int(input("Enetr the number of which table you want: "))
i = 1

while i <= 10:
    print(num, "X" ,i, "=", num*i)
    i += 1