#Task 4
#Roll 2 Dice at random and add them

import random

dice = [1, 2, 3, 4, 5, 6]
first_throw = random.choice (dice)
second_throw = random.choice (dice)
final = first_throw + second_throw

print ("First dice: " + str(first_throw) + "   Second dice: " + str(second_throw))

print ("You can move " + str(final) + " spaces.")