weight = float(input("Please enter your weight in pounds."))
height = float(input("Please enter your height in inches."))
bmi = 0
condition = 0

calcBMI(height,weight):
    return weight/(height*height)* 703

if bmi <=18.5:
    conhsition = "underweight"
elif bmi <=24.9:
    condition = "normal"
elif bmi <=29.9:
    condition = "overweight"
elif bmi <=34.9:
    condition = "obese"
elif bmi <=39.9:
    condition = "very obese"
else:
    condition = "morbidly obese"

print("Your BMI is:", calcBMI(height,weight))
print("You are", condition)
