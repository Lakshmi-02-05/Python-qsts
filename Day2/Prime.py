#Print numbers from 1 to 50.


for i in range(2,51):
    is_Prime = True

    for n in range(2,i):
        if i % n == 0:
            is_Prime = False
            break;

    if is_Prime:
        print(i,"is Prime number")