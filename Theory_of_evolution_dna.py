with open("dna.txt") as myfile:
    x = myfile.read()
    x = list(x)
    print(x)
    print(len(x))

import random
def evolve(x):
    # x is a list so size will be 0 to len(x)-1
    ind = random.randint(0,len(x)-1) # index of variable of particular bit in which change has to take place
    # this change is actually depend on the variable p
    p = random.randint(1,100)
    print(p)
    if(p==1):
        if(x[ind]=='0'):
            x[ind]='1'
        else:
            x[ind]='0'
for i in range(len(x)):
    evolve(x)

print(x)

# exploring random libray
'''
with open("file1.txt","r+") as myfile:
    # r, w, a and r+ used for read and write both
    print(myfile.read())
    myfile.write("I am Rishu Kumar ")
    print(myfile.read())
myfile.close()
'''
import random
print(random.randint(1,5))
# randint is used to generate a random integer in the given range, here including 1 and 5 and between them

print(random.randrange(1,5))
# it generates number from lowerlimit(0 by default) to upperlimit-1

print(random.random())
# it will generate decimal number from 0 to 1

print(random.randrange(1,10,2))
# 2 is step. it will generate only odd numbers

print(random.randrange(0,11,2))
# it will generate even numbers from 0-10


print(random.choice([1,2,3,5,7,10]))
# it generates random numbers from given list

