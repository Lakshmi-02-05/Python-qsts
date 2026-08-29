#Ask the user for a string and reverse it.

text = input("Enter a string: ")
# print(text[::-1])

# OR

reverse = ""

for char in text:
    reverse = char + reverse

print("Reverse word is: ",reverse)