weight = float(input("Please enter your weight in pounds."))
height = float(input("Please enter your height in inches."))
bmi = 0
condition = 0

def calcBMI(height,weight):
    global bmi
    bmi = weight/(height*height)* 703
    if bmi <=18.5:
        return "underweight"
    elif bmi <=24.9:
        return "normal"
    elif bmi <=29.9:
        return "overweight"
    elif bmi <=34.9:
        return "obese"
    elif bmi <=39.9:
        return "very obese"
    else:
        return "morbidly obese"
    
condition = calcBMI(height,weight)
print("Your BMI is:", bmi)
print("You are", condition)
