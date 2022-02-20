import random

from hangman_word import word_list

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

output_ascii_hangman_start = """
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

stages = [output_ascii_hangman_start,
          output_ascii_hangman_head,
          output_ascii_hangman_torso,
          output_ascii_handman_right_arm,
          output_ascii_hangman_left_arm,
          output_ascii_hangman_right_leg,
          output_ascii_hangman_left_leg]

output_blank = " _ "


def choose_word(word_list):
    return random.choice(word_list)


def check_guess(chosen_word, guess):

    if chosen_word.count(guess) == 0:
        return False

    else:
        return True


def generate_word_field(chosen_word, word_field):

    for char in chosen_word:

        word_field.append(output_blank)

    return word_field


def get_letter_index(chosen_word, guess):

    letter_index_location = []

    for item in range(len(chosen_word)):

        if chosen_word[item] == guess:

            letter_index_location.append(item)

    return letter_index_location


def add_letter_to_field(chosen_word, guess, word_field):

    num_guessed_letter = chosen_word.count(guess)

    while num_guessed_letter > 0:

        char_indexes = get_letter_index(chosen_word, guess)

        word_field[char_indexes[num_guessed_letter - 1]] = guess

        num_guessed_letter -= 1

    return word_field


def main():

    word_field = []
    end_of_game = False
    stage_count = 0
    stage = stages[0]
    print(msg_title)

    print(output_ascii_hangman_start)

    chosen_word = choose_word(word_list)

    print(f"Chosen word is: {chosen_word}")

    word_field = generate_word_field(chosen_word, word_field)

    print(word_field)

    while not end_of_game:

        guess = input("Guess a letter: ").lower()

        if check_guess(chosen_word, guess) == True:

            print(stage)

            print(add_letter_to_field(chosen_word, guess, word_field))

        else:

            stage_count += 1

            stage = stages[stage_count]

            if stage != output_ascii_hangman_left_leg:

                print(stage)

                print(word_field)

                print(f"\nWord does not contain {guess}\n Try again")

        if ' _ ' not in word_field or stage == output_ascii_hangman_left_leg:

            print(f'Word was: {chosen_word}')

            print(output_ascii_hangman_left_leg + "\n\nGAME OVER")

            end_of_game = True


main()
