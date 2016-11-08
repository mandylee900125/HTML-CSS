number = int(input("Enter a number "))
num = number
rev = 0

def getReverse():
    global num,rev
    while num > 0:
        rev = rev*10
        rev = rev + num%10
        num = int(num/10)
    return rev

print(number,"reverse is", getReverse())
        
