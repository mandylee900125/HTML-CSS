r = float(input("Enter interest rate:"))
p = int(input("Enter principle:"))
n = int(input("Enter the number of times the loan in compunded per year:"))
t = int(input("Enter number of years:"))

def interest(p,r,n,t):
    output= "{:10.2f}".format((p*((1+(r/n))**(n*t))/(t*12)))
    return output

print ("Your payment amout is :", interest(p,r,n,t), "dollars")
   



