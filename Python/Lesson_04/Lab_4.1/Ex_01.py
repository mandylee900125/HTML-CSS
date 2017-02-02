item1 = input("Please enter item 1:")
price1 = float(input("Please enter the price:"))
item2 = input("Please enter item2:")
price2 = float(input("Please enter the price:"))
item3 = input("Please enter item3:")
price3 = float(input("Please enter the price:"))
subtotal = price1+ price2+price3
tax = subtotal*0.075
total = tax + subtotal


print("{:<<10}{:_^15}{:>>10}".format("","Receipt",""))

def printr(item,price):
    print("{:<0}{:>10}{:<10}{:>10.2f}".format("*",item," ........",price))

item = item1
price = price1
printr (item, price)

item = item2
price = price2
printr(item, price)

item = item3
price = price3
printr (item, price)

item = "Subtotal"
price = subtotal
printr (item,price)

item = "Tax"
price = tax
printr (item,price)

item = "Total"
price = total
printr (item,price)

print("____________________________________")
print(" * Thank you for your support *")




