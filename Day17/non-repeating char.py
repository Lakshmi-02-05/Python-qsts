# Find the first non-repeating character

text = "swiss"
non_repeating_char = None
for char in text:
    if text.count(char) == 1:
        non_repeating_char = char
        break

    if non_repeating_char:
        print("First non-repeating character:", non_repeating_char)
    else:
        print("No non-repeating character found.")