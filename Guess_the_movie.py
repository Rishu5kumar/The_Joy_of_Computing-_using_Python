import random

movies = ['inception', 'exmachina', 'drishyam', 'titanic', 'junglebook', 'anbe sivan', 'gol maal', 'vikram vedha', 'black friday', 'dangal', 'taare zameen par']

def create_question(movie):
    n = len(movie)
    letters = list(movie)
    temp = []
    for i in range(n):
        if(letters[i]==' '):
            temp.append(' ')
        else:
            temp.append('*')
    qn = ''.join(str(x) for x in temp)
    return qn

def is_present(character, movie):
    cnt = movie.count(character)
    if cnt == 0:
        return False
    return True
    #if character is in movie:
    #    return True
    #return False

def unlocked(qn, movie, letter):
    ref = list(movie)
    qn_list = list(qn)
    temp = []
    for i in range(len(movie)):
        if(ref[i] == ' ' or ref[i] == letter):
            temp.append(ref[i])
        else:
            if qn_list[i] == '*':
                temp.append('*')
            else:
                temp.append(ref[i])
                # temp.append(qn_list[i])
    modi_qn = ''.join(str(x) for x in temp)
    return modi_qn

def play():
    p1name = input("Player 1, Enter your name: ")
    p2name = input("Player 2, Enter your name: ")
    pp1 = 0
    pp2 = 0
    turn = 0
    willing = True
    while(willing):
        if(turn%2 == 0):
            # player 1
            print(p1name, " Your turn")
            picked_movie = random.choice(movies)
            question = create_question(picked_movie)
            print(question)
            modified_question = question
            not_said = True
            while(not_said):
                character = input("Your guessed letter: ")
                if(is_present(character, picked_movie)):
                    modified_question = unlocked(modified_question, picked_movie, character)
                    print(modified_question)
                    decision = int(input("Press 1 to guess the movie or 2 to unlock another letter: "))
                    if(decision == 1):
                        answer = input("Enter Your answer: ")
                        if answer == picked_movie:
                            pp1 += 1
                            print("Correct answer:)")
                            not_said = False
                            print(p1name, "Your score is:", pp1)
                        else:
                            print("Wrong answer:(, Try again!")
                else:
                    print(character, "not found:(")
            choice = int(input("Press 1 to continue or 0 to quit: "))
            if choice == 0:
                print(p1name, "Your score:", pp1)
                print(p2name, "Your score:", pp2)
                print("Thanks for playing, Have a nice day!")
                willing = False
        else:
            print(p2name, " Your turn")
            picked_movie = random.choice(movies)
            question = create_question(picked_movie)
            print(question)
            modified_question = question
            not_said = True
            while(not_said):
                character = input("Your guessed letter: ")
                if(is_present(character, picked_movie)):
                    modified_question = unlocked(modified_question, picked_movie, character)
                    print(modified_question)
                    decision = int(input("Press 1 to guess the movie or 2 to unlock another letter: "))
                    if(decision == 1):
                        answer = input("Enter Your answer: ")
                        if answer == picked_movie:
                            pp2 += 1
                            print("Correct answer:)")
                            not_said = False
                            print(p1name, "Your score is:", pp2)
                        else:
                            print("Wrong answer:(, Try again!")
                else:
                    print(character, " not found:(")
            choice = int(input("Press 1 to continue or 0 to quit: "))
            if choice == 0:
                print(p1name, "Your score:", pp1)
                print(p2name, "Your score:", pp2)
                print("Thanks for playing, Have a nice day!")
                willing = False
        turn += 1
play()
