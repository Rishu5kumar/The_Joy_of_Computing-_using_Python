'''
There are some sort of coupons was available and you have to bet on one particular coupon then draw coupon randomly from the available list of coupon and if your betted coupon and the coupon that appears matches you will win, for playing this game you are supposed to place some amount and if you win you get something much more than what you have paid.

Let there are 10 coupons and each coupon contain a digit from one to ten so one number is present in each coupon you are supposed to bet something say i say the number seven will appear if you draw now i will say that so now after listening
to my bet seven they will draw a coupon randomly, if that randomly drawn coupon contains the number seven i win else i lose let i pay 100 rupees so if i win i will get much more what i pay or else i will lose 100.
'''

# We can check the memory usage of an object x using the command sys.getsizeof(x)

import random
import matplotlib.pyplot as plt
# import this # by writing this we can print "zen of python"

account = 0
x = []
y = []

for i in range(365):
    x.append(i+1)
    bet = random.randint(1,10)
    lucky_draw = random.randint(1,10)

    # print("Bet:",bet)
    # print("Lucky Draw:",lucky_draw)

    if bet==lucky_draw:
        account += 900-100 # net gain is 800 rs
    else:
        account -= 100
    y.append(account)
print("Amount, in your game account:",account)

plt.plot(x,y)
plt.title("Gambling Visualization")
plt.xlabel("Days")
plt.ylabel("Money Gained/Lost")
plt.show()
