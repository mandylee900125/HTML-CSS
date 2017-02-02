class Cars:
   def __init__(self,p="",i="",e="",t=""):
        self.paint = p
        self.interior = i
        self.engine = e
        self.tires = t

    def setCustom(self,newp,newi,newe,newt):
        self.paint = newp
        self.interior = newi
        self.engine = newe
        self.tires = newt

    def getPaint(self):
        return self.paint
    
    def getInterior(self):
        return self.interior

    def getEngine(self):
        return self.engine

    def getTires(self):
        return self.tires

def main():
    p = input("Enter the paint of your vehicle: ")
    i = input("Enter the interior of your vehicle: ")
    e = input("Enter the engine of your vehicle: ")
    t = input("Enter the tires of your vehicles: ")

    user1 = Cars(p,i,e,t)
    print("\nYour vehicle is ready......\n")
    print("Paint:     ", user1.getPaint(), "\nInterior:     ", user1.getInterior(), "\nEngine:     ", user1.getEngine(), "\nTires:     ", user1.getTires())
    
main()


class Human:
    def __init__(self,h,e,s):
        self.hair = h
        self.eyes = e
        self.skin = s

    def setHES(self,newH,newE,newS):
        self.hair = newH
        self.eyes = newE
        self.skin = newS

    def getHair(self):
        return self.hair

    def getEyes(self):
        return self.eyes

    def getSkin(self):
        return self.skin

def main():

    h = input("Enter hair color: ")
    e = input("Enter eyes color: ")
    s = input("Enter skin color: ")

    user1 = Human(h,e,s)

    print("\nMy info...\n")
    print("Hair: ", user1.getHair(), "\nEyes: ", user1.getEyes(), "\nSkin: ", user1.getSkin())

    user1.setHES("blonde", "blue", "white")

    print("\nFriend's info...")
    print("Hair: ", user1.getHair(), "\nEyes: ", user1.getEyes(), "\nSkin: ", user1.getSkin())

main()    
    



    
        
    
        





















