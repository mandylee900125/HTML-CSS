def main(h,l,w):
    h = int(input("Enter the height in inches:"))
    l = int(input("Enter the length in inches:"))
    w = int(input("Enter the width in inches:"))
    print ("The volume of your subwoofer box is", calcVol(h,l,w),"cubic feet")

def calcVol(h,l,w):
    volume = (h*12)*(l*12)*(w*12)
    return volume

 print ("The volume of your subwoofer box is", calcVol(h,l,w),"cubic feet")



