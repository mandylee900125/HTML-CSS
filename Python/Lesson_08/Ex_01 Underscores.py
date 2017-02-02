sentence = input("Enter a sentence" )

def replace(sentence):
   if 0 == sentence.count(" "):
      return sentence
   else:
      return replace(sentence[0:sentence.index(" ")]+ "_" + sentence[sentence.index(" ")+1 : len(sentence)])

print(replace(sentence))                 
