import random

def rock_paper_scissors():
    choices = ['rock', 'paper', 'scissors']
    play_again = 'y'

    while play_again.lower() == 'y':
        computer_choice = random.choice(choices)
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        while user_choice not in choices:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

        print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            print("You win!")
        else:
            print("Computer wins!")

        play_again = input("\nDo you want to play again? (y/n): ")
        while play_again.lower() not in ['y', 'n']:
            print("Invalid input. Please enter y or n.")
            play_again = input("Do you want to play again? (y/n): ")

rock_paper_scissors()
