# Count vowels in a string

text = "Python Programming Is Amazing"
t1 = text.lower()
vowels = "aeiou"
count = 0
for char in t1:
    if char in vowels:
        # count = count + 1
        count += 1

print(f"The number of vowels in the string is: {count}")