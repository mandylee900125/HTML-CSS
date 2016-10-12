num1 = 5
num2 = 7
num3 = 9

def calcAvg(one,two,three):
    return (one+two+three)/3

def numPrint(one,two,three):
    avg = calcAvg(one,two,three)
    print("The average of", one,two,"and",three, "is",avg)


numPrint(num1,num2,num3)
