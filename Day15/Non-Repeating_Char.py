# Find the first non-repeating character

text = "aabbccdef"
char_count = {}

for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Find the first non-repeating character
for char in text:
    if char_count[char] == 1:
        print(f"The first non-repeating character is: {char}")
        break
    else:
        print("No non-repeating character found.")