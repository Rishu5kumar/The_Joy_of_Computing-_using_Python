import string
import random
# print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

symbols = []
symbols = list(string.ascii_letters)
card1 = [0]*5
card2 = [0]*5

# i need to find the position of the same symbol in card 1 as well as in card 2
pos1 = random.randint(0,4)
pos2 = random.randint(0,4)
# pos1 ans pos2 are the same symbol positions in card1 and card2 respectively

samesymbol = random.choice(symbols)
symbols.remove(samesymbol) # we don't want same symbol to repeat in card1 and card2
if(pos1==pos2):
    card2[pos1]=samesymbol
    card1[pos1]=samesymbol
else:
    card1[pos1]=samesymbol
    card2[pos2]=samesymbol
    card1[pos2]=random.choice(symbols)
    symbols.remove(card1[pos2])
    card2[pos1]=random.choice(symbols)
    symbols.remove(card2[pos1])
i=0
while i<5:
    if(i!=pos1 and i!=pos2):
        alphabet1 = random.choice(symbols)
        symbols.remove(alphabet1)
        alphabet2 = random.choice(symbols)
        symbols.remove(alphabet2)
        card1[i] = alphabet1
        card2[i] = alphabet2
    i+=1
print(card1)
print(card2)

ch = input("Spot the similar symbol: ")
if(ch==samesymbol):
    print("Right")
else:
    print("Wrong")


'''
l1 = ['A', 'B', 'G', 'T', 'F', 'C']
l2 = ['T', 'J', 'Y', 'P', 'O', 'L']
def check(l1,l2):
    if len(l1)!=len(l2):
        return False
    if l1 is None or l2 is None:
        return False
    for i in l1:
        for j in l2:
            if i==j:
                return True
    return False
print(check(l1,l2))
'''
