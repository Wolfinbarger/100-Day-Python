import random

msg_title = """

88                                                                            
88                                                                            
88                                                                            
88,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYb,d8 88,dPYba,,adPYba,  ,adPPYYba, 8b,dPPYba, 
88P'    "8a ""     `Y8 88P'   `"8a a8"    `Y88 88P'   "88"    "8a ""     `Y8 88P'   `"8a  
88       88 ,adPPPPP88 88       88 8b       88 88      88      88 ,adPPPPP88 88       88 
88       88 88,    ,88 88       88 "8a,   ,d88 88      88      88 88,    ,88 88       88 
88       88 `"8bbdP"Y8 88       88  `"YbbdP"Y8 88      88      88 `"8bbdP"Y8 88       88 
                                    aa,    ,88                                
                                     "Y8bbdP"                                 
"""

acsii_hangman_start = """
  +---+
  |   |
      |
      |
      |
      |
=========
"""

output_ascii_hangman_head = """
  +---+
  |   |
  O   |
      |
      |
      |
=========
"""

output_ascii_hangman_torso = """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
"""

output_ascii_handman_right_arm = """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
"""

output_ascii_hangman_left_arm = """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
"""

output_ascii_hangman_right_leg = """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
"""

output_ascii_hangman_left_leg = """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
"""
word_list = ["aardvark", "baboon", "camel"]


def choose_word(word_list):
    return random.choice(word_list)


def check_guess(chosen_word, guess):
    if chosen_word.count(guess) == 0:
        return False
    else:
        return True


def main():

    print(msg_title)

    chosen_word = choose_word(word_list)

    guess = input("Guess a letter: ").lower()

    print(check_guess(chosen_word, guess))


main()
