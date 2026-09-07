#Word Length Dictionary

sentence = "Python is very powerful language"
words = sentence.split()
word_lngth ={}
for word in words:
    word_lngth[word] = len(word)

print(word_lngth)