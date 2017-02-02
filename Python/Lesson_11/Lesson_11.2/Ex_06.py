import random
class Inventory:
    def __init__(self, m, n, c = "", p = ""):
        self.manufacture = m
        self.name = n
        self.catagory = c
        self.UPC = random.randint(0,1000000000)
        self.price = p

    def getInfo(self, newM, newN, newC):
        self.manufacture = newM
        self.name = newN
        self.catagory = newC

    def getManufacture(self):
        return self.manufacture

    def getName(self):
        return self.name

    def getCatatogry(self):
        return self.catagory

    def getUPC(self):
        return self.UPC

    def getPrice(self):
        return self.price

    def __str__(self):
        print("Your item...\nManufacture: ", self.manufacture, "\nName: ", self.name, "\nCatagory", self.catagory, "\nUPS: ", self.UPC, "\nPrice: ",self.price) 

def main():
    m = input("Please enter the manufacture: ")
    n = input("Please enter the name: ")
    yn = input("Will you be entering catrgory and price information? y or n ")
    
    

    if yn == 'n':
        item1 = Inventory(m,n)
    if yn == 'y':
        c = input("Please enter the catagory: ")
        p = int(input("Please enter the price: "))
        item1 = Inventory(m,n,c,p)
    print(item1.__str__())

main()
