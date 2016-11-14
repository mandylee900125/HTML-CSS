word1 = input("Enter word1 ")
word2 = input("Enter word2 ")
word3 = input("Enter word3 ")

def makeCenter(word):
    if len(word) >= 20:
        return word
    else:
        return makeCenter(" "+ word + " ")

print(makeCenter(word1))
print(makeCenter(word2))
print(makeCenter(word3))
