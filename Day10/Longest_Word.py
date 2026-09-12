#Find the longest word without repeating characters

words = ["apple", "banana", "world", "python", "programming"]
longest = ""

for word in words:
    if len(word) > len(longest) and len(set(word)) == len(word):
        longest = word
print(f"The longest word without repeating characters is: {longest}")
