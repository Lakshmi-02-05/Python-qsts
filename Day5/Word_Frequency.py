#Word Frequency

text = "python is easy and python is Powerful"
def word_freq(text):
    freq = {}
    words = text.lower().split()
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

print(word_freq(text))