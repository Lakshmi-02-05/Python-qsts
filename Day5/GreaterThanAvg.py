#Find Numbers Greater Than Average

num = [10, 20, 30, 50, 40]
def greater_avg(num):
    total = sum(num)
    avg = total / len(num)
    result = []  
    for n in num:
        if n > avg:
            result.append(n)     
    return min(result)  

print(greater_avg(num))  