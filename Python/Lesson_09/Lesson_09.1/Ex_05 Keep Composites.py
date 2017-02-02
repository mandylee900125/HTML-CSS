nums = [2,6,8,9,10,12,23,15,17,24,55,66,78,77,79]

def gFactor(number):
    for l in range(2, number):
        if number % l == 0:
            return 1
    return 0
def removePrimes(num):
    for n in num:
        if gFactor(n) == 0:
            num.remove(n)
            

removePrimes(nums)
print(nums)

    
