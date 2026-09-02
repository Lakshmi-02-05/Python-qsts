# #Create a Function that should tell the user three things:
# Whether the number is positive/negative/zero
# Whether it is even/odd
# Whether it is prime/not prime

def number(num):
    if num > 0:
        pn_num = f"{num} is positive number"
    elif num < 0:
        pn_num = f"{num} is negative number"
    else:
         pn_num = f"You entered Zero"

    if num % 2 == 0:
        eo_num = f"{num} is an Even number"
    else:
        eo_num = f"{num} is an Odd number"

    for i in range(2,num):
        if num % i == 0:
            prime = f"{num} is not a Prime number"
        else:
            prime = f"{num} is a Prime number"


    return f"{pn_num}, \n{eo_num}, \n{prime}"


print(number(21))