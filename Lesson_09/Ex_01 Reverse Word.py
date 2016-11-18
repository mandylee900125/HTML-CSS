def reverse(word):
    line = ""
    for i in range(len(word)-1,-1,-1):
        line += word[i]
    print(line)

words = input("pleas enter line:")
print("In order...")
print("words")
print(" ")
print("Reversed...")
reverse(words)

