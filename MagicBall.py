# Task 5
# Create a Magic Eight Ball type of game

print ("Hello there!")
question = input("Hit me with a Question!  " )

import random
print ("...")
print (random.choice(list(open("magic.txt"))))