side = float(input("Enter the side:"))

def calcSurf():
    global surface
    surface = "{:10.5f}".format((side*side)*6)

def printl():
    print("The surface area of a cube whos side are", side, "in length is", surface,".")

calcSurf()
printl()
