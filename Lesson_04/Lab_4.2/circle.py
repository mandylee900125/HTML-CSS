r = float(input("Enter the radius:"))

def calcArea(r):
    area = "{:6.5}".format(r*r*3.14)
    return area
def printl(r):
    print("The area of a circle with a radius of" ,r, "is" ,calcArea(r),".")

printl(r)
