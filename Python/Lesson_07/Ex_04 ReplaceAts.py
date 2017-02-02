sentence = input("Enter a sentence ")

def replace():
    global sentence
    while sentence.count("a") > 0:
        sentence = sentence.replace("a","@")
replace()
print(sentence)

