word = input("Enter a word ")

def printl():
    for i in range(len(word),-1,-1):
        print(word[i:len(word)])
printl()

