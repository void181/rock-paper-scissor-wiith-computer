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

#Write your code below this line 👇

import random
game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock,1 for Paper or 2 for Scissors.\n"))
user_choice = int(user_choice)  

game_images=game_images[user_choice]
print("userchoiceis"+game_images)

game_images = [rock, paper, scissors]
computer_choice=game_images
computer_choice = random.randint(0,2)
game_images=game_images[computer_choice]
print("computer choice"+game_images)
