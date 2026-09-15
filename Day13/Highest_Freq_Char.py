# Find the character with the highest frequency

text = "programming"
char_freq = {}
for char in text:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1

highest_freq_char = max(char_freq, key=char_freq.get)
print(f"Highest freq char is{highest_freq_char} : {char_freq[highest_freq_char]}.")