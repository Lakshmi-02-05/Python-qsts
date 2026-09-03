#Create a function that shows Largest number: 1.Smallest number, 2.Sum, 3.Number of even values, 4.Number of odd values, 5.Average

numbers = [10, 25, 8, 43, 12, 7]
def analyze_list(numbers):
    print("Smallest Number: ",min(numbers))

    sum = 0
    for num in numbers:
        sum += num 

    even_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1

    odd_count = 0
    for num in numbers:
        if num % 2 != 0:
            odd_count += 1

    avg = sum/len(numbers)

    return f"Sum:{sum} \nEven Number Count: {even_count} \nOdd Number Count: {odd_count} \nAverage Value: {avg}"

print(analyze_list(numbers))