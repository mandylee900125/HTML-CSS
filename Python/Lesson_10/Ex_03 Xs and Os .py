import random 
xAndO = []

for i in range (0,4):
    xAndO.append([])
        for j in range (0,4):
            switch = random.randint(0,1)
            if switch == 1:
                xAndO[i] += "X"
            else:
                xAndO += "O"
for i in xAndO:
    output = ""
    for j in i:
        output += j
    print(output)
