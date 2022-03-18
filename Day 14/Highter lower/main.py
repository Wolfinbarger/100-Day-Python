from random import choice
from unicodedata import name
from game_data import data
import art
import os


wrong_answer = False

player_score = 0


def random_data():
    return choice(data)


def format_data(comparison):
    name = comparison["name"]
    descr = comparison["description"]
    country = comparison["country"]
    return f"{name}, a {descr}, from {country}"


def check_guess(player_guess, a_follower_count, b_follower_count):
    if player_guess == 'a' and a_follower_count > b_follower_count:
        return True
    elif player_guess == 'b' and b_follower_count > a_follower_count:
        return True
    return False


print(art.logo)

compare_b = random_data()

while not wrong_answer:

    compare_a = compare_b
    compare_b = random_data()

    while compare_a == compare_b:
        compare_b = random_data()

    print(f"Compare A: {format_data(compare_a)}.")

    print(art.vs)

    print(f"Compare B: {format_data(compare_b)}.")

    player_guess = input(
        "Who has the more followers? Type 'A' or 'B': ").lower()

    a_follower_count = compare_a["follower_count"]
    b_follower_count = compare_b["follower_count"]

    os.system('cls' if os.name == 'nt' else 'clear')

    if check_guess(player_guess, a_follower_count, b_follower_count) == True:
        player_score += 1
        print(f"You're right! Current score: {player_score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {player_score}\n")
        wrong_answer = True
