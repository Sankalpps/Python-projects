import random
while True:
    print("---------------Welcome------------------------")
    player_score=0
    computer_score=0
    tie=0
    print("Choose any one among this")
    print("1.Rock 2.Paper 3.Scisor")
    choice=int(input("Enter the number"))
    print()
    while choice > 3 or choice < 1:
        print(input("Your value is incorrect"))
    if choice==1:
        player_choice="Rock"
    elif choice==2:
        player_choice="Paper"
    else:
        player_choice="Scisor"
    print("The player's choice is:",player_choice)
    print("Now it's computer's turn")
    computer=random.randint(1,3)
    if computer==1:
        computer_choice="Rock"
    elif computer==2:
        computer_choice="Paper"
    else:
        computer_choice="scisor"
    print("Computer's choice is:",computer_choice)
    if player_choice=="Rock" and computer_choice=="Paper" or  player_choice=="Paper" and computer_choice=="Rock":
        Result="Paper"
    elif player_choice=="scisor" and computer_choice=="Paper" or  player_choice=="Paper" and computer_choice=="scisor":
        Result="scisor"
    elif player_choice=="Rock" and computer_choice=="scisor" or  player_choice=="scisor" and computer_choice=="Rock":
        Result="Rock"
    elif(player_choice==computer_choice):
        Result=tie
    if Result==tie:
        tie +=1
    if Result==player_choice:
        player_score +=1
    if Result==computer_choice:
        computer_score +=1
    print("Player score is:",player_score)
    print("Computer score is:",computer_score)
    print("Tie",tie)

