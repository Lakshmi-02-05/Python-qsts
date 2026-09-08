#First Non-Repeating Character

text = "aabbcddeeo"
for char in text:
    if text.count(char) == 1:
        print("The first non-repeating character is:", char)
        break