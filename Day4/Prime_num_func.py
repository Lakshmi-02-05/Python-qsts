#5. Prime Number Function

def prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
        else:
            return True

print(prime(11))