import random
while True:
    print("---------WELCOME TO MY PROJECT---------- ")
    user_score=0
    comp_score=0
    Tie=0
    name=input("Please enter your name : ")
    print("1.Rock  2.Paper  3.Scissor")
    choice=int(input("Enter your choice"))
    print()
    while choice > 3 or choice < 1:
        print(input("Number enterded is invalid"))
    if choice==1:
        user_choice="Rock"
    elif choice==2:
        user_choice="Paper"
    else:
        user_choice="Scisor"
    print("The users choice is",user_choice)
    print("Now it is computer's turn")
    computer=random.randint(1,3)
    if computer==1:
        comp_choice="Rock"
    if computer==2:
        comp_choice="Paper"
    if computer==3:
        comp_choice="Scisor"
    print("comp choice is ",comp_choice)
    if (user_choice=="Rock" and comp_choice =="Paper") or (user_choice=="Paper" and comp_choice=="Rock"):
        print("Paper wins")
        Result="Paper"
    elif (user_choice=="Scisor" and comp_choice =="Paper") or (user_choice=="Paper" and comp_choice=="Scisor"):
        print("Scisor wins")
        Result="Scisor"
    elif (user_choice=="Rock" and comp_choice =="Scisor") or (user_choice=="Scisor" and comp_choice=="Rock"):
        print("Rock wins")
        Result="Rock"
    elif(user_choice==comp_choice):
        print("Tie")
    if Result=="Tie":
        tie=+1
    elif Result==user_choice:
        user_score=+1
    else:
        comp_score=+1
    print("Scores are")
    print(name,"'s score is",user_score)
    print("Computer's score is",comp_score)

    repeat="Do ypu want to play again"
    if repeat=="No" or repeat=="no":
        break
