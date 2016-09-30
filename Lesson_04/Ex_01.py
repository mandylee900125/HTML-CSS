item1 = input("Please enter item 1:")
price1 = float(input("Please enter the price:"))
item2 = input("Please enter item2:")
price2 = float(input("Please enter the price:"))
item3 = input("Please enter item3:")
price3 = float(input("Please enter the price:"))


print("{:<<10}{:_^15}{:>>10}".format("","Receipt",""))

def printr(item,price):
    print("{:<0}{:>10}{:<10}{:>10.10}".format("*",item," ........",price))

item = item1
price = price1
printr (item, price)

item = item2
price = price2
printr(item, price)

item = item3
price = price3
printr (item, price)

print("____________________________________")
print(" * Thank you for your support *")




