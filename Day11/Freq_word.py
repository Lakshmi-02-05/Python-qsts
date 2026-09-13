# Count frequency of each word

sentence = "python is easy and python is powerful"

for word in sentence.split():
    freq = sentence.count(word)
    print(f"{word}:{freq}")