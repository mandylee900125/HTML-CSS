num = int(input("Enter an interger "))
size = int(input("Enter table size"))

print("__|__")
for i in range(1,size,1):
    print("{:>0}|{:<0}".format(i+1,num*(i-1)))
