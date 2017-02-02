math = input("Please enter your letter grade for math ")
science = input("Please enter your letter grade for science ")
english = input("Please enter your letter grade for english ")
history = input("Please enter your letter grade for history ")
pe = input("Please enter your letter grade for P.E ")
art = input("Please enter your letter grade for art ")
language = input("Please enter your letter grade for language ")
grade = 0

def calcPoints(grade):
    if grade == "a":
        return 4.0
    if grade == "b":
        return 3.0
    if grade == "c":
        return 2.0
    if grade == "d":
        return 1.0
    if grade == "f":
        return 0


GPA = (calcPoints(math)+calcPoints(science)+ calcPoints(english)+calcPoints(history)+calcPoints(pe)+calcPoints(art)+calcPoints(language))/7
print("Your GPA is",GPA)
