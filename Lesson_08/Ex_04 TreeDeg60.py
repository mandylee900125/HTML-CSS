word = input("Enter a word ")
start = 1
stop = len(word)

def tree(word,start,stop):
    if start <= stop:
        print(word[0:start])
        start = start +1
        tree(word,start,stop)
        
tree(word,start,stop)
