import random
numList = []

for i in range(0,4):
    numList.append([])
    for j in range(0,4):
        numList[i].append(random.randint(1,100))
        
for nums in numList:
    output = ""
    for num in nums:
        output += str(num) + " "
    print(output)

