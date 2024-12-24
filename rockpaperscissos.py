import random
# Variables
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
game_rounds = 0


def play_game():
    def player_choice():

        if your_choice == "0":
            print(rock)
        if your_choice == "1":
            print(paper)
        if your_choice == "2":
            print(scissors)

    player_choice()
    computer_choice = random.choice(game_images)

    input(f"Computer chose: {computer_choice}")
    
    def game_score():
        user_score = 0
        computer_score = 0
        if your_choice == "0" and computer_choice == paper:
            print("You lose")
            computer_score += 1
        elif your_choice == "0" and computer_choice == scissors:
            print("You win!")
            user_score += 1
        elif your_choice == "1" and computer_choice == rock:
            print("you win!")
            user_score += 1
        elif your_choice == "1" and computer_choice == scissors:
            print("You lose")
            computer_score += 1
        elif your_choice == "2" and computer_choice == rock:
            print("you lose")
            computer_score += 1
        elif your_choice == "2" and computer_choice == paper:
            print("you win")
            user_score += 1
        else:
            print("Draw")
        
    game_score()


while game_rounds <= 10:
    your_choice = input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors. ")
    game_rounds += 1
    play_game()
    