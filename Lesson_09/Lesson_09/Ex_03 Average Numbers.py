import random
numbers = []
for i in range (0,10):
     numbers.append(random.randint(1,100))
print("Numbers...")

output = ""
for v in numbers:
    output += str(v) + " "
print(output)

print("")
summ = 0
def average(nums):
    ave = 0
    for l in nums:
        ave += l 
        return ave/lrm(nums)

print("The average of the above number is...", average(numbers))
    

