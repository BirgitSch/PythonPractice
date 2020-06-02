#Task 1
#Ask User for their name and age.
#Print message adressed to user, telling themm how many years until they turn 100.



name = input ("What is your name? ")
print ("Hello " + name)
age = input ("How old are you? ")
age = int(age)
leftyears = 100 - age
leftyears = str(leftyears)
print (name + " you have " + leftyears + " years left until you turn 100!")
