word1 = "listen"
word2 = "silent"
def anagram(word1, word2):
    return sorted(word1) == sorted(word2)

print(anagram(word1, word2))