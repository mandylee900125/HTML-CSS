r = float(input("Enter the radius:"))

def calcArea():
    global area
    area ="{:6.5}".format((r*r)*3.14)

def printl():
    print("The area of a circle with a radius of" ,r, "is" ,area,".")

calcArea()
printl()
