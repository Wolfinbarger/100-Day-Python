from multiprocessing import RLock
import random


rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
msg_win = "YOU WIN!!"

msg_lose = "YOU LOSE"

hand_gesture = [rock, paper, scissor]

computer_selected_gesture = ['rock', 'paper', 'scissor']

random.seed(10)
random_num = random.randint(1, 3)


computer_guess = hand_gesture[random_num - 1]
computer_selected = computer_selected_gesture[random_num - 1]


user_choice = input('Choose between: "Rock", "Paper", "Scissor" ').lower()

if user_choice == 'rock':
    select_gesture = 0
elif user_choice == 'paper':
    select_gesture = 1
else:
    select_gesture = 2

print(f"You chose:\n + {hand_gesture[select_gesture]}")

print(f"Computer chose:\n{computer_guess}")

if hand_gesture[select_gesture] == computer_guess:
    print('DRAW!!!')
elif user_choice == 'rock' and computer_selected == 'scissor':
    print(msg_win)
elif user_choice == 'scissor' and computer_selected == 'paper':
    print(msg_win)
elif user_choice == 'paper' and computer_selected == 'rock':
    print(msg_win)
else:
    print(msg_lose)
