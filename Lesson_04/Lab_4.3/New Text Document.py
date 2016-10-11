num1 = int(input("NUM:"))
num2 = 7
num3 = 0

def setNums():
    global num1,num2
    num1 = 8
    num2 = 13

def addNums():
    global sum
    sum = num1 + num2

setNums()
addNums()
print(sum)
