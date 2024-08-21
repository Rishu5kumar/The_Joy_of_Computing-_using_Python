import random
import threading

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

def timeout(event):
    print("\nTime's up! You didn't answer in time.")
    event.set()  # Set the event to signal that time is up

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

        time_up_event = threading.Event()  # Create an event object

        # Start the timer thread
        timer = threading.Timer(60, timeout, [time_up_event])
        timer.start()

        # Get the player's answer only if time has not expired
        ans = None
        try:
            ans = input("What is in my mind? ")

            if not time_up_event.is_set():  # Check if time is not up
                if ans == picked_word:
                    if turn % 2 == 0:
                        pp1 += 1
                        print("Your score is", pp1)
                    else:
                        pp2 += 1
                        print("Your score is", pp2)
                else:
                    print("Better luck next time, I thought:", picked_word)
            else:
                print("Sorry I can't accept your answer as you didn't answer in time.")
        except Exception:
            print("Time's up!")

        # Cancel the timer
        timer.cancel()

        # Check if the user wants to continue or quit
        c = int(input("Press 1 to continue and 0 to quit: "))
        if c == 0:
            thank(p1name, p2name, pp1, pp2)
            break

        turn += 1

play()

