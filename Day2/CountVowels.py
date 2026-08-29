#Ask the user to enter a string and count how many vowels (a, e, i, o, u) it contains.

str = input("Enter your string value: ")
count = 0

for char in str:
    if char in "aeiou":
        count += 1

print("Vowels: ",count)