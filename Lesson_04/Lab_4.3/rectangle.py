l = float(input("Enter the length:"))
w = float(input("Enter the width:"))

def calcPerim():
    global perimeter
    perimeter = "{:10.5}".format((l+w)*2)

calcPerim()
print("Your rectngle is", perimeter, "ft round.")
    
    
