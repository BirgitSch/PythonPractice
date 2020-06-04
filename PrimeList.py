#How many prime numbers are there between 0-100? Work with a list.
#Check if a given number is a prime number between 0-100 using the list.

list = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
nr = str(len(list))
print ("There are " + nr + " prime numbers between 0 and 100.")

yournr = input ("Which number should I check for you? ")

if int(yournr) > 100:
    print (str(yournr) + " is not a number between 0 and 100!")
elif int(yournr) in list:
    print (str(yournr) + " is a prime number!")
else:
    print (str(yournr) + " is not a prime number!")