item1 = input("Please enter item 1:")
price1 = float(input("Please enter the price for item 1:"))
item2 = input("Please enter item 2:")
price2 = float(input("Please enter the price for item 2:"))
item3 = input("Please enter item 3:")
price3 = float(input("Please enter the price for item 3:"))
item4 = input("Please enter item 4:")
price4 = float(input("Please enter the price for item 4:"))
subtotal = price1+ price2+ price3+ price4
tax = subtotal* 0.075
discount = 0
total = subtotal- discount+ tax

def discountl(subtotal, discount):
    if subtotal >= 2000:
        discount = subtotal*0.15
        return discount
    if subtotal <= 2000:
        discount = 0
        return discount
        
def formatl(item,price):
    print("*{:<13}........{:>5.2f}*".format(item,price))
          
          
print("<<<<<<<<<<< Receipt >>>>>>>>>>>>>>")
formatl (item1, price1)
formatl (item2, price2)
formatl (item3, price3)
formatl (item4, price4)
formatl ("Subtotal", subtotal)
formatl ("Discount", discountl(subtotal,discount))
formatl ("Tax",tax)
formatl ("Total",total)
print("____________________________________")
print(" * Thank you for your support *")




        
    
