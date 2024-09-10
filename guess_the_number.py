import random

number = random.randint(1,5)
attempt = 1
n = int(input("Enter components:"))
while(n>0):
    user_num = int(input("Enter the number:"))
    if(user_num==number and attempt==1):
        print("GENIOUS- Take a BOW")
        break
    elif(user_num==number and attempt>1):
        print("YOU WIN with",attempt,"attempts")
        break
    elif(user_num>number):
        print("Too big")
        attempt += 1
        n -= 1
    else:
        print("Too small")
        attempt += 1
        n -= 1
    if(n==0):
        print("sorry")
