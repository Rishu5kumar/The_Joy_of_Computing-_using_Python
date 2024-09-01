def rock_paper_scissor(num1, num2, bit1, bit2):
    p1 = int(num1[bit1])%3
    # p1 is the placeholder at bit position bit1 in num1 and will mod with 3 as inputted nos. will be decimal but we want answer in zero, one and two so will do mod 3

    p2 = int(num2[bit2])%3

    if(player_one[p1]==player_two[p2]):
        print("Draw")
    elif(player_one[p1]=="Rock" and player_one[p2]=="Scissor"):
        print("Player one wins!")
    elif(player_one[p1]=="Rock" and player_one[p2]=="Paper"):
        print("Player two wins!")
    elif(player_one[p1]=="Paper" and player_one[p2]=="Scissor"):
        print("Player two wins!")
    elif(player_one[p1]=="Paper" and player_one[p2]=="Rock"):
        print("Player one wins!")
    elif(player_one[p1]=="Scissor" and player_one[p2]=="Rock"):
        print("Player two wins!")
    elif(player_one[p1]=="Scissor" and player_one[p2]=="paper"):
        print("Player one wins!")

player_one = {0:'Rock', 1:'Paper', 2:'Scissor'}
player_two = {0:'Paper', 1:'Rock', 2:'Scissor'}

while(1):
    num1 = input("Player one, Enter your choice:")
    num2 = input("Player two, Enter your choice:")
    # we have to make the user input the secret bit position for player one and two
    bit1 = int(input("Player one, Enter the secret bit position: ")) # 0 to number of digits-1
    bit2 = int(input("Player two, Enter the secret bit position: ")) # 0 to number of digits-1


    rock_paper_scissor(num1,num2,bit1, bit2)
    ch = input("Do you want to continue? (y/n):")
    if(ch=='n'):
        break
