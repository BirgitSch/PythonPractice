#Task 6
#Make half pyramid out of input word





[word for word in "word" ]
a = []
word = input ("Give me a Word to make art out of?  ")
word = word.lower()
b = len(word)

for row in range(b):
    for col in range(row+1):
        print (word[col], end="")
    print ()

