import random
player = random.randint(1,6)
computer = random.randint(1,6)

def rollDice():
    print("You rolled a", player)
    print("Computer rolled a", computer)
    if player > computer:
        print("The winner is you")
    if computer > player:
        print("The winner is computer")

rollDice()



