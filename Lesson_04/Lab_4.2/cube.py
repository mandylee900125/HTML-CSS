side = float(input("Enter the side:"))

def calcSurf(side):
    surface = "{:10.5f}".format((side*side)*6)
    return surface
def printl(side):
    print("The surface area of a cube whos side are", side, "in length is", calcSurf(side),".")

printl(side)
