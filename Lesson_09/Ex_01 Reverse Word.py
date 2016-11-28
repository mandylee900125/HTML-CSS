words =  ["Freddy", "Mike", "Lisa", "Alan", "Frank"]
print("In order...")
for word in words:
    print

print(" ")
print("Reversed...")

def reverse(word):
    line = ""
    for i in range(len(word)-1,-1,-1):
        line += word[i]
    print(line)
    
reverse(words)

