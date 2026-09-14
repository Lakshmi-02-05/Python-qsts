# Find the first non-repeating character

text = "aabbcdeeff"
for char in text:
    if text.count(char) ==1:
        print("First Non-Repeating Char is:", char)
        break

    