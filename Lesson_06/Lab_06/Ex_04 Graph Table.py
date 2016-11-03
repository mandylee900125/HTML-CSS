num = int(input("Enter an interger "))
size = int(input("Enter table size "))

print("_|_")
for i in range(1,size+2):
    print("{:>0}|{:<0}".format(i-1,num*i))
