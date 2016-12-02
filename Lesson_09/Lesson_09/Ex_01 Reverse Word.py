words =  ["Freddy", "Mike", "Lisa", "Alan", "Frank"]
print("In order...")
output = ""
for i in words:
    output += i + " "
print(output)

print(" ")
print("Reversed...")


def reverse(word):
    a = ""
    for l in range(len(word)-1,-1,-1):
        a += word[l]+ " "
    print(a)
    
reverse(words)

