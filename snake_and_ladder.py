from PIL import Image
import random
end = 100

def show_board():
    img = Image.open('snake.jpeg')
    img.show()

def check_ladder(score):
    if score == 3:
        print("Ladder")
        return 20
    elif score == 6:
        print("Ladder")
        return 14
    elif score == 11:
        print("Ladder")
        return 28
    elif score == 15:
        print("Ladder")
        return 34
    elif score == 17:
        print("Ladder")
        return 74
    elif score == 22:
        print("Ladder")
        return 37
    elif score == 38:
        print("Ladder")
        return 59
    elif score == 49:
        print("Ladder")
        return 67
    elif score == 57:
        print("Ladder")
        return 76
    elif score == 61:
        print("Ladder")
        return 78
    elif score == 73:
        print("Ladder")
        return 86
    elif score == 81:
        print("Ladder")
        return 98
    elif score == 88:
        print("Ladder")
        return 91
    else:
        # no ladder
        return score

def check_snake(score):
    if score == 8:
        print("Snake")
        return 4
    elif score == 18:
        print("Snake")
        return 1
    elif score == 26:
        print("Snake")
        return 10
    elif score == 39:
        print("Snake")
        return 5
    elif score == 51:
        print("Snake")
        return 6
    elif score == 54:
        print("Snake")
        return 36
    elif score == 56:
        print("Snake")
        return 1
    elif score == 60:
        print("Snake")
        return 23
    elif score == 75:
        print("Snake")
        return 28
    elif score == 83:
        print("Snake")
        return 45
    elif score == 85:
        print("Snake")
        return 59
    elif score == 90:
        print("Snake")
        return 48
    elif score == 92:
        print("Snake")
        return 25
    elif score == 97:
        print("Snake")
        return 87
    elif score == 99:
        print("Snake")
        return 63
    else:
        return score

def reached_end(score):
    if score == end:
        return True
    return False

def play():
    p1_name = input("Player 1, Enter your name:") # same as raw_input() used in 2.x
    p2_name = input("Player 2, Enter your name:")
    pp1 = 0 # initial points of player 1
    pp2 = 0 # initial points of player 2

    turn = 0
    while(1):
        if turn % 2 == 0:
            print(p1_name, "Your Turn!")
            c = int(input("Press 1 to continue or press 0 to exit:"))
            if c == 0:
                print(p1_name,"scores",pp1)
                print(p2_name,"scores",pp2)
                print("Quitting the game, Thank You!")
                break
            dice = random.randint(1,6)
            print("Dice Showed",dice)
            pp1 += dice
            pp1 = check_ladder(pp1)
            pp1 = check_snake(pp1)
            if pp1 > end:
                pp1 = end

            print(p1_name,"Your Score:",pp1)

            if reached_end(pp1):
                print(p1_name,"WON")
                break
        else:
            print(p2_name, "Your Turn!")
            c = int(input("Press 1 to continue or press 0 to exit:"))
            if c == 0:
                print(p1_name,"scores",pp1)
                print(p2_name,"scores",pp2)
                print("Quitting the game, Thank You!")
                break
            dice = random.randint(1,6)
            print("Dice Showed",dice)
            pp2 += dice
            pp2 = check_ladder(pp2)
            pp2 = check_snake(pp2)
            if pp2 > end:
                pp2 = end

            print(p2_name,"Your Score:",pp2)

            if reached_end(pp2):
                print(p2_name,"WON")
                break

        turn += 1

show_board()
play()
