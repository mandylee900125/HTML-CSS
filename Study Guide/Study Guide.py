area = 0
radius = 6

def calcRadius():
    global area
    area = 3.14*(radius**2)

def radPrint():
    print("The radius of your circle is{:0.3f}".format(area))
calcRadius()
radPrint()

