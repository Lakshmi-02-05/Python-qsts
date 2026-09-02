#7. Count Vowels Using a Function

def vowels(str):
    count = 0
    for char in str:
        if char in "aeiou":
            count += 1
    return count

print(vowels("Hello Lakshmi, Welcome to the world of python"))