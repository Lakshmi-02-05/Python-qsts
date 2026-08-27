#Reverse a number without converting it to a string.

# num = "123456"
# reverse = num[::-1]
# print(reverse)
#.  OR


# num = "123456"
# reverse = " "
# for char in num:
#     reverse = char + num
# print(reverse)
#.  OR

num = 123456
num1 = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print(num1, "reverse is",reverse)