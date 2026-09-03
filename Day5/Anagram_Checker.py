#Anagram Checker: Two words are anagrams if they contain the same letters in a different order.
# listen → silent ✅
# triangle → integral ✅
# hello → world ❌

word1 = "listen"
word2 = "silent"
def is_anagram(word1,word2):
    return sorted(word1) == sorted(word2)
        
print(is_anagram(word1,word2))