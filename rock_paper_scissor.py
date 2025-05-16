import random


your_score = 0
computer_score = 0

Total_rounds = int(input("How many rounds do you want to play? :"))
round_no = 1

while Total_rounds >= round_no :
    print("Choices :\n1.Rock\n2.Paper\n3.Scissors")

    your_choice = int(input(" Enter your choice :"))


    if your_choice == 1 :
        your_choice_name = 'Rock'
    elif your_choice == 2 :
        your_choice_name = 'Paper'
    else :
        your_choice_name = 'Scissor'


    computer_choice = random.randint(1,3)
    if computer_choice == 1 :
        computer_choice_name = 'Rock'
    elif computer_choice == 2:
        computer_choice_name = 'Paper'
    else:
        computer_choice_name = 'Scissor'

    print(" Your choice : " , your_choice_name
          , "  , Computer's choice = " , computer_choice_name)


    if your_choice == computer_choice :
        your_score = your_score
        computer_score = computer_score
        round_no+=1

        print("it's a tie!")
        print("your score = " , your_score , " ,  computer's score = " , computer_score)


    elif (your_choice == 1 and computer_choice == 2) or (your_choice==2 and computer_choice==3) or (your_choice==3 and computer_choice==1)  :
        your_score = your_score
        computer_score+=1
        round_no+=1
        print("computer wins!")
        print("your score = " , your_score , "computer's score = " , computer_score)


    elif (your_choice == 1 and computer_choice == 3) or (your_choice==2 and computer_choice==1) or (your_choice==3 and computer_choice==2) :
        your_score+=1
        computer_score= computer_score
        round_no+=1
        print("You win!")
        print("your score = ", your_score, ", computer's score = ", computer_score)

print("\n-------GAME OVER---------")
print("\nYour final score :" , your_score , ", Computer's final score :" , computer_score)

if your_score> computer_score :
    print("You won the game!")

elif your_score< computer_score :
    print("Computer won the game!")

else :
    print("It's a tie overall!")

while True:

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing!")
    break















