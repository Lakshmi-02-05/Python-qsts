#Group Numbers : Separate into Even and Odd numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_num = []
odd_num = []
for num in numbers:
    if num % 2 == 0:
        even_num.append(num)
    else:
        odd_num.append(num)

print("Even Num:", even_num, "\nOdd Num: ", odd_num)



#Using Dictionary
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = {
#     "even": [],
#     "odd": []
# }
# for num in numbers:
#     if num % 2 == 0:
#         result["even"].append(num)
#     else:
#         result["odd"].append(num)
# print(result)