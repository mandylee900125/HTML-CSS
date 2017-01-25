import random
class UserC:
    def __init__(self, fName = "" , lName = "" , avat = ""):
        self.firstName = fName
        self.lastName = lName
        self.avatar = avat
        self.userID = random.randint(0,1000000)

    def getInfo(self,newFName,newLName,newAvat):
        self.firstName = newFName
        self.lastName = newLName
        self.avatar = newAvat
        self.userID = random.randint(0,1000000)

    def getFirst(self):
        return self.firstName

    def getLast(self):
        return self.lastName

    def getAvatar(self):
        return self.avatar

    def getUserID(self):
        return self.userID
    
    def __str__(self):
        return "Customer Info...\nFirst Name: ", self.firstName, "\nLast Name: "

def main():
    fName = input("Please enter your first name")
    lName = input("Please enter your last name")
    yn = input("Do you want a public avatar?y or n.")

    if yn == "n":
        user1 = UserC(fName,lName)
    if yn == "y":
        avatar = input("Please enter your avatar")
        user1 = UserC(fName, lName, avatar)
    print(user1.__str__())

main()

        
        
        
