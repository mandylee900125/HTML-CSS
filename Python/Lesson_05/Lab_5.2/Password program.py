def passCheck():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == "iamhappy" and password == "iamhappytoo":
        print("You are granted access!")
    else:
        if username == "iamhappy":
            print("Your password is incorrect")
        elif password == "iamhappytoo":
            print("Your username is incorrect")
        else:
            print("Your username and password are incorrect")
passCheck()
        
    
