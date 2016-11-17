
word = input("Enter a word ")
start = 1
stop = len(word)

def tree(word,start,stop):
    if start <= stop:
        print("{:>10}".format(word[0:start]))
        start = start + 1
        tree(word,start,stop)
    else:
        return " "
        
tree(word,start,stop)
