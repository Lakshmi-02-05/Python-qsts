#Remove Duplicates Using a Function

numbers = [1, 2, 2, 3, 4, 3, 5, 1, 6]
# def remove_duplicate(numbers):
#     print(set(numbers))
# remove_duplicate(numbers)

#OR
def remove_duplicate(numbers):
    n = []
    for num in numbers:
        if num not in n:
            num.append(n)
        return n
remove_duplicate(numbers)   