#Count Even and Odd Numbers in a list

list = [23,43,54,66,5,3,1,8]
even_count = 0
odd_count = 0

for num in list:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count  += 1

print("Even Count: ", even_count)
print("Odd Count: ", odd_count)
        
    


