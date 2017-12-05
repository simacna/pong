import string
shakes = "methinks it is like a weasel"

# write a function that generates a string that is 27 characters long 
# by choosing random letters from the 26 letters in the alphabet plus the space. 
# We’ll write another function that will score each generated string by comparing 
# the randomly generated string to the goal.

# A third function will repeatedly call generate and score, then if 100% of 
# the letters are correct we are done. If the letters are not correct then we will 
# generate a whole new string.To make it easier to follow your program’s progress this third function 
# should print out the best string generated so far and its score every 1000 tries.

a = list(map(chr, range(97, 123)))
alphabet = a.append(' ')
print(a)

