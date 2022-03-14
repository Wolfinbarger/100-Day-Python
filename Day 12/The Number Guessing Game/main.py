from art import logo

import messages as msg

from random import randint

easy_attempts = 10

hard_attempts = 5


def is_correct(player_guess, computer_number):
    """Checks if player guess is correct"""
    if player_guess == computer_number:
        return True
    return False


def set_player_attempts(difficulty):
    """Sets player attempts"""
    if difficulty == 'easy':
        return easy_attempts
    return hard_attempts


def is_player_high_or_low(player_guess, computer_number):
    """Checks if player is high or low"""
    if player_guess < computer_number:
        return msg.msg_too_low
    return msg.msg_too_high


def main():
    player_guess_corret = False

    print(logo + msg.msg_welcome)

    difficulty = input(msg.msg_choose_difficulty).lower()

    player_attempts = set_player_attempts(difficulty)

    computer_number = randint(1, 100)

    while player_attempts != 0 or not player_guess_corret:
        player_guess = int(input(msg.msg_make_guess))

        if is_correct(player_guess, computer_number) is True:
            player_guess_corret = True
            print(msg.msg_correct)
            break
        elif player_attempts == 1:
            print(msg.msg_lose)
            print(f"The correct answer was: {computer_number}")
            break
        else:
            player_attempts -= 1
            print(is_player_high_or_low(player_guess, computer_number))
            print(msg.msg_guess_again)
            print(
                f"You have {player_attempts} attempts remaining to guess the number.")


main()
