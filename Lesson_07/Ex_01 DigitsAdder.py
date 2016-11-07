number = int(input("Enter an interger "))
Sum = 0
num = number

while num > 0:
    Sum = Sum + num%10
    num = int(num/10)
    
print("The sum of the digits in", number, "is", Sum)
    
    
