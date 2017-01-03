go = input("Please enter 16 strings: ")
spList = go.split(" ")
wordList = []

spot = 0
for i in range (0,4):
    output = ""
    wordList.append([])
    for j in range (0,4):
        wordList[i].append(spList[spot])
        output += wordList[i][j] + "\t"
        spot += 1
    print(output)
        
