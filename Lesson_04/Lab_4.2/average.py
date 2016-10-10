num1 = float(input("Enter number 1:"))
num2 = float(input("Enter number 2:"))
num3 = float(input("Enter number 3:"))

def average(num1,num2,num3):
        ave = "{:10.5f}".format((num1+num2+num3)/3)
        return ave
def printl(num1,num2,num3):
        print("The average of",num1,",",num2,", and",num3,"is",average(num1,num2,num3),".")

printl(num1,num2,num3)

