import random
import time

def choose():
    words = ["rainbow", "computer", "science", "programming", "mathematics", "player", "condition", "reverse", "water", "board"]
    pick = random.choice(words)
    return pick

def jumbled(word):
    qn = "".join(random.sample(word, len(word)))
    return qn

def thank(p1name, p2name, pp1, pp2):
    print(p1name, "Your score is:", pp1)
    print(p2name, "Your score is:", pp2)
    print("Thanks for playing!")
    print("Have a nice day!")

def play():
    p1name = input("Player 1, Enter your name? ")
    p2name = input("Player 2, Enter your name? ")
    pp1 = 0
    pp2 = 0
    turn = 0
    while True:
        picked_word = choose()
        qs = jumbled(picked_word)
        print(qs)

        if turn % 2 == 0:
            print(p1name, "Your turn.")
        else:
            print(p2name, "Your turn.")

        start_time = time.time()
        ans = None
        while True:
            ans = input("What is in my mind? ")
            elapsed_time = time.time() - start_time
            if elapsed_time <= 60:
                break
            else:
                print("\nTime's up! You didn't answer in time.")
                ans = None
                break

        if ans == picked_word:
            if turn % 2 == 0:
                pp1 += 1
                print("Your score is", pp1)
            else:
                pp2 += 1
                print("Your score is", pp2)
        # elif ans is None:
            # print("Your score for this turn is 0. Moving on to the next player...")
        else:
            print("Better luck next time, I thought:", picked_word)

        c = int(input("Press 1 to continue and 0 to quit: "))
        if c == 0:
            thank(p1name, p2name, pp1, pp2)
            break

        turn += 1

play()


'''
import random
def choose():
    words = ["rainbow", "computer", "science", "programming", "mathematics", "player", "condition", "reverse", "water", "board"]
    pick = random.choice(words)
    return pick

def jumbled(word):
    qn = "".join(random.sample(word, len(word)))
    return qn

def thank(p1name, p2name, pp1, pp2):
    print(p1name, "Your score is:", pp1)
    print(p2name, "Your score is:", pp2)
    print("Thanks for playing!")
    print("Have a nice day!")

def play():
    p1name = input("Player 1, Enter your name? ")
    p2name = input("Player 2, Enter your name? ")
    pp1 = 0
    pp2 = 0
    turn = 0

    while True:
        picked_word = choose()
        qs = jumbled(picked_word)
        print(qs)

        start_time = time.time()
        elapsed_time = 0

        if turn % 2 == 0:
            print(p1name, "Your turn.")
        else:
            print(p2name, "Your turn.")

        while elapsed_time < 60:
            ans = input("What is in my mind? ")
            elapsed_time = time.time() - start_time

            if ans == picked_word:
                if turn % 2 == 0:
                    pp1 += 1
                    print("Your score is", pp1)
                else:
                    pp2 += 1
                    print("Your score is", pp2)
                break
            else:
                print("Better luck next time, I thought:", picked_word)
                break
        else:
            print("Time's up! The correct word was:", picked_word)

        c = int(input("Press 1 to continue and 0 to quit: "))
        if c == 0:
            thank(p1name, p2name, pp1, pp2)
            break

        turn += 1

play()
'''

"""
import random
def choose():
    words = ["rainbow", "computer", "science", "programming", "mathematics", "player", "condition", "reverse", "water", "board"]
    pick = random.choice(words)
    return pick
def jumbled(word):
    qn = "".join(random.sample(word,len(word))) # it is returned as a list
    # "".join() combines all words/alphabets irrespective of a separator
    return qn

def thank(p1name, p2name, pp1, pp2):
    print(p1name, " Your score is: ", pp1)
    print(p2name, " Your score is: ", pp2)
    print("Thanks for playing!")
    print("Have a nice day!")

def play():
    p1name = input("Player 1, Enter your name?")
    p2name = input("Player 2, Enter your name?")
    pp1 = 0
    pp2 = 0
    turn = 0
    while(1):
        picked_word = choose()
        qs = jumbled(picked_word)
        print(qs)
        if(turn % 2 ==0):
            print(p1name, " Your turn. ")
            ans = input("What is in my mind?")
            if(ans == picked_word):
                pp1+=1
                print("Your score is ", pp1)
            else:
                print("Better luck next time, I thought: ", picked_word)
            c = int(input("Press 1 to continue and 0 to quit"))
            if(c==0):
                thank(p1name, p2name, pp1, pp2)
                break
        else:
            print(p2name, "Your turn. ")
            ans = input("What is in my mind?")
            if(ans == picked_word):
                pp2+=1
                print("Your score is ",pp2)
            else:
                print("Better luck next time, I thought: ", picked_word)
            c = int(input("Press 1 to continue and 0 to quit"))
            if(c==0):
                thank(p1name, p2name, pp1, pp2)
                break
        turn+=1
play()
"""
