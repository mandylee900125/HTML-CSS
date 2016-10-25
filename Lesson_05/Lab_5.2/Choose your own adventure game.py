choice = input("You are in a cave and there's two roads infront of you, do you choose to go 'left' or 'right'")


def game():
    if choice == right:
        num = int(input("You choose the right path. Now guess a number between 1 and 5"))
        if num == num5:
            choice = input("You picked the right number! There's an apple infront of you do you choose to eat it.'yes' or 'no')
                if choice == yes:
                    print("The apple is poisonous u lose!")
                else:
                    print("The apple is poisonous you win!)
        else:
            num = int("You choose the wrong number. Last chance, guess again.")
                if num ==5:
                    print("You guessed it right, you win!")
                else:
                    print("You guessed it wrong, you lose!")

    else:
        num = int(input("You choose the wrong path. Now guess a number between 1 and 5"))
        if num == num5:
            choice = input("You picked the right number! There's an apple infront of you do you choose to eat it.'yes' or 'no')
                if choice == yes:
                    print("The apple is poisonous u lose!")
                else:
                    print("The apple is poisonous you win!)
        else:
            num = int("You choose the wrong number. Last chance, guess again.")
                if num ==5:
                    print("You guessed it right, you win!")
                else:
                    print("You guessed it wrong, you lose!")
    
