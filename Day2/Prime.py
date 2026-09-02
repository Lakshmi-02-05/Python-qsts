#Print numbers from 1 to 50.


for i in range(2,51):
    is_Prime = True

    for n in range(2,i):
        if i % n == 0:
            is_Prime = False
            break;

    if is_Prime:
        print(i,"is Prime number")

# for i in range(1, 51):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)