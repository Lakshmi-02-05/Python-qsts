#6. Find the Largest Using a Function

def largest__num(num):
    largest = num[0]
    for n in num:
        if n > largest:
            largest = n
    return largest

print(largest__num([23,34,45,56,54,43,33]))