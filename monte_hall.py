'''
In the Monty Hall problem, there are three doors in total, and behind these doors:

- Two doors have a goat each (prize that is generally considered undesirable in the context of the game).
- One door has a car (the desired prize).

The Monty Hall problem is a probability puzzle based on a game show scenario. Here's a brief overview of how it works:

1. The contestant is presented with three closed doors. Behind one of the doors is a car, and behind the other two doors are goats.
2. The contestant picks one of the three doors, but does not open it.
3. The host, Monty Hall, who knows what's behind all the doors, then opens one of the remaining two doors to reveal a goat.
4. Monty then gives the contestant the option to either stick with their original choice or switch to the other unopened door.

The counterintuitive solution to the problem shows that switching doors increases the contestant's chances of winning the car from 1/3 to 2/3. This is because the initial choice had a 1/3 chance of being the car, and if the contestant switches, they benefit from the 2/3 probability that their first choice was a goat.
'''

import random
doors = [0]*3
goatdoor = [0]*2
swap = 0 # no. of swap wins
dont_swap = 0 # no. of don't swap wins
j=0
while(j<10):
    x = random.randint(0,2) # xth door will comprise of car
    doors[x] = "BMW"
    for i in range(0,3):
        if(i==x):
            continue
            # if i write continue it will go to start of the loop since xth door is already comprise of the BMW
            # so we only need to take into the count the doors except x 
            # we are not considering the x here, we are only considering the doors that comprise of goat 
        else:
            doors[i] = "Goat"
            goatdoor.append(i)
        # so two of them comprise goat and one comprise BMW
    choice = int(input("Enter your choice: "))

    door_open = random.choice(goatdoor)
    # open the door that comprise of a goat

    # door_open and choice shouldn't be same
    while(door_open == choice):
        door_open = random.choice(goatdoor)

    ch = input("Do you want to swap(y/n):")
    if(ch=='y'):
        if(doors[choice]=="Goat"):
            print("Player Wins")
            swap+=1
            # if ch=='y' means player is chosen to swap then we have to take care the fact that if he has chosen the goat in initial stage in initial choice then if he swaps here then obviously he will get a BMW because already a door comprising of goat has been opened and a door that has goat he has chosen in its initial stage and now he is swapping, now if he will swap he will get a BMW
        else:
            print("Player Lost")
    else:
        if(doors[choice]=="Goat"):
            print("Player Lost")
        else:
            print("Player Wins")
            dont_swap+=1
    j+=1

print("Swap wins is:",swap)
print("Don't swap wins is:",dont_swap)
