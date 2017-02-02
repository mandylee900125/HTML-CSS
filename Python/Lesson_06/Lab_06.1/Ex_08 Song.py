word1 = "Na "
word2 = "Hey "
word3 = "Goodbye!"
output = ""

def s(word, times,output):
    for i in range (1,times+ 1):
        output = output + word + " "
        if i == times:
            print(output)
        
s(word1,4,output)
s(word1,4,output)
s(word2,3,output)
s(word3,1,output)
