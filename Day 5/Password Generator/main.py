# Password Generator Project
import random
from re import I


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

new_password = ""
for num in range(0, nr_letters):
    index = random.randint(0, 51)
    new_password += new_password.join(letters[index])


for num in range(0, nr_symbols):
    index = random.randint(0, 8)
    new_password += new_password.join(symbols[index])

for num in range(0, nr_numbers):
    index = random.randint(0, 9)
    new_password += new_password.join(numbers[index])

print("Easy:\n" + new_password)
# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

hard_new_password = []

for num in range(0, nr_letters):
    index = random.randint(0, 51)
    hard_new_password.append(letters[index])


for num in range(0, nr_symbols):
    index = random.randint(0, 8)
    hard_new_password.append(symbols[index])

for num in range(0, nr_numbers):
    index = random.randint(0, 11)
    hard_new_password.append(numbers[index])


new_password = ''

for num in range(0, len(hard_new_password)):
    index = random.randint(0, len(hard_new_password) - 1)
    new_password += new_password.join(hard_new_password[index])
    hard_new_password.pop(index)


print("\nHard:\n" + new_password)

# more elegant way is to use the .choice()
