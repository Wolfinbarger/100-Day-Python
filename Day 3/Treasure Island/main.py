import random
from urllib import response


print('''
        __________
        /\____;;___\\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
''')

print("""
You've just landed on Treasure Island.
Find the treasure!!!
""")

you_win = "You found the treasure!"

game_over = "Game Over"
game_over_fell = "Fall into a hole.\n" + game_over
game_over_attacked = "Attacked by knife wielding crab\n" + game_over
game_over_eaten = "Eaten by the local dinosaurs\n" + game_over
game_over_fire = "Burned alive in a fire\n" + game_over

game_continue = True

switcher = {
    1: 'You are at a tree. Do you wish to go "left" or "right"? ',
    2: 'You are at a river that cuts through the island. Do you "wait" or "swim"? ',
    3: 'There are three doors. One blue, one red, one yellow and one green.\n Which do you choose? '
}

while(game_continue):

    random_number = random.randint(1, 3)

    if random_number == 1:

        response = str(input(switcher[random_number])).lower()

    elif random_number == 2:

        response = str(input(switcher[random_number])).lower()

    else:
        response = str(input(switcher[random_number])).lower()

    if response == "right":

        print(game_over_fell)

        game_continue = False

    elif response == "swim":

        print(game_over_attacked)

        game_continue = False

    elif response == "red":

        print(game_over_fire)

        game_continue = False

    elif response == "blue":

        print(game_over_eaten)

        game_continue = False

    elif response == "yellow":

        print(you_win)

        game_continue = False
