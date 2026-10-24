# Check whether a string is a palindrome

text = "Anna"
t1 = text.lower()
t2 = t1[::-1]
if t1 == t2:
    print(text, "is a palindrome")
else:
    print(text, "is not a palindrome")