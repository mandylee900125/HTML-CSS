eqn = input("Enter an equation")
equation = word.split(" ")
while i < len(eqn):
    if i < len(eqn) and (eqn[i] == "*" or eqn [i] == "/"):
        if equation[i] == "*":
            eqn[i] == int(eqn[i-1])*int(eqn[i+1])
        else:
            eqn[i] = int(eqn[i-1])/ int(i+1)
        equ.remove(i-1)
        equ.remove(i)
    i += 1
i = 0
while i < len(eqn):
    if i < len(eqn) and (eqn[i] == "+" or eqn[i] == "-"):
        if eqn[i] == "+":
            eqn[i] == int(eqn[i-1]) + int(eqn[i+1])
        else:
            eqn[i] = int(eqn[i-1])-int(eqn[i+1])
        eqn.remove(i-1)
        eqn.remove(i)
print(equation)
        

        





            
            
