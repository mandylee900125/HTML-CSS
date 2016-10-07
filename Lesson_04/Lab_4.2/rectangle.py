length = float(input("Enter the length:"))
width = float(input("Enter the width:"))

calcPerim (length,width)
    perimeter = "{:10.5f}".format((length + width)*2)
    return perimeter
print()
    output = "Your rectangle is", calcPerim (length,width), "ft around."

    
