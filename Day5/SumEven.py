#Sum of Even Numbers

numbers = [10, 15, 22, 7, 8, 13, 20]
def sum_even(numbers):   
    num = [ ]
    for n in numbers:
        if n % 2 == 0:
            num.append(n)
    sum = 0
    for i in num:
        sum += i
    return f"Sum of the even numbers is: {sum}"

print(sum_even(numbers))