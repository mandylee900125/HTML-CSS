length = float(input("Enter the length:"))
width = float(input("Enter the width:"))

def calcPerim(length,width):
    perimeter = "{:10.5f}".format((length + width)*2)
    return perimeter
def printl():
    print("Your rectangle is", calcPerim (length,width), "ft around.")


printl()    
