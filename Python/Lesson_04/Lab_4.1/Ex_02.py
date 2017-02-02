firstName = input ("Enter your first name:")
lastName = input ("Enter your last name:")
title = input ("Enter yor title:")
school =  input ("Enter school site:")
year = input ("Enter school year:")
subject = input ("What is your subject?")

def printi (first,last):
  print("{:<2}{:>13}{:>18}{:>1}".format("* ", first, last," *"))

print("*"*35)

first = school
last = year
printi (first, last)

first = firstName
last = lastName
printi (first, last)

first = title
last = subject
printi (first, last)

print ("*"*35)

