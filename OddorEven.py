#Task 2
#Is a given number even or odd?

num = input ("Type in a number between 0 and 100. ")
num = int(num)
nummod = num % 2
nummod = int(nummod)

if num > 100:
    print ("Not a Number between 0 and 100!")

elif nummod == 0 :
    print (str(num) + " is an even Number.")
else :
    print (str(num) + " is an odd Number.")

