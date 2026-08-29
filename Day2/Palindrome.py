# Ask the user for a word and determine whether it is a palindrome.

text = input("Enter a sring: ")
reverse = ""
for char in text:
    reverse = char + reverse

    if text == reverse:
        print(text,"is a Palindrome")
    else:
        print(text,"is not a Palindrome")


