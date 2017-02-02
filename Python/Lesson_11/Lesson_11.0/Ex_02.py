import math
class Distance:
    def __init__(self,x1,y1,x2,y2):
        self.xOne = x1
        self.yOne = y1
        self.xTwo = x2
        self.yTwo = y2
        self.distance = 0
        
    def setValues(self,newX1,newY1,newX2,newY2):
        self.xOne = newX1
        self.yOne = newY1
        self.xTwo = newX2
        self.yTwo = newY2
        self.distance = 0

    def getMPH(self):
        self.distance = math.sqrt((self.xTwo-self.xOne)*(self.xTwo-self.xOne)+(self.yTwo-self.yOne)*(self.yTwo-self.yOne))
        return self.distance

def main():
    x1 = int(input("Enter a number for x1: "))
    y1 = int(input("Enter a number for y1: "))
    x2 = int(input("Enter a number for x2: "))
    y2 = int(input("Enter a number for y2: "))
    
    user1 = Distance(x1,y1,x2,y2)

    print("distance = ",user1.getMPH() )

main()
