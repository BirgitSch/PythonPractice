#Task8
#Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
#and makes a new list of only the first and last elements of the given list.
#For practice, write this code inside a function.
import random


my_list = []
for i in range(10):
    n = random.randint(1,20)
    my_list.append(n)
print("This is my random list:" + str(my_list))

def my_list_function ():
    print("This is the first number in my list: " + str(my_list[0]))
    print("This is the last number in my list: " + str(my_list[9]))

my_list_function ()

equals = my_list[0] + my_list[9]
print ("If I add the first number of my list and the last number of my list I get: " + str(equals))
        


