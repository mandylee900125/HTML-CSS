import random
numbers = []
for i in range (0,10):
    numbers[i] = random.randint(1,100)
print("numbers...")

output = ""
for v in numbers:
    output += v + " "
print(output)

print("")
summ = 0
def average(nums):
    ave = 0
    for l in nums:
        ave += l
        summ += 1
        return ave/summ

print("The average of the above number is...", average(numbers))
    
