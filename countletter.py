#Task 7
#Count Letter in text

with open("cagedbird.txt") as f:
    first_line = f.readline()
    text = f.read()
    
    #print (text)

def count_car (text,char):
    count=0
    for c in text:
        if c == char:
            count +=1
    return count

letter= input ("Which letter should I count? ")
print("I counted the " + letter +":")
print(count_car(text, letter))
print("times in this wonderful Poem:")
print(first_line)
