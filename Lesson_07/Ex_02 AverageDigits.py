number = int(input("Enter a number "))
digits = 0
average = 0

def avDigits():
    global num,digits,average
    num = number
    while num > 0:
        digits += 1
        average = average + num%10
        num = int(num/ 10)
    return average/digits

print("The average of the digits in" ,number, "is" ,avDigits())
        

