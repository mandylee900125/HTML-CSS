num1 = int(input("Enter a number "))
num2 = int(input("Enter a another number "))
output = " "

for i in range (num2,num1+num2,num2):
    output = output + str(i)+ "\t"
print(output)


          

