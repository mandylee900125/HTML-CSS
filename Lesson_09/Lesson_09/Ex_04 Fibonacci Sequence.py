start = int(input("Pleaase enter your staring number:"))
size = int(input("Please enter your sequence size:"))
seq = []
for i in range(0,size):
    if i == 0 or i==1:
        seq[i] = start
    else:
        seq[i] = seq
    print(seq[i]," ")
