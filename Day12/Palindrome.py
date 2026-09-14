# Check whether a string is a palindrome ignoring spaces and case

text = "Never Odd Or Even"
t = text.replace(" ", "").lower()
if t == t[::-1]:
    print(f"'{text}', is a palindrome")