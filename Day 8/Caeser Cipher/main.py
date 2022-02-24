from art_ascii import title_caeser_cipher
from encrypt import encrypt
from decrypt import decrypt
from caeser import caeser


# if direction == "encode":

#     encrypt(plain_text=text, shift_amount=shift)

# else:

#     decrypt(cipher_text=text, shift_amount=shift)

restart = ""

while restart != 'no':
    print(title_caeser_cipher + "\n\n")

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    text = input("Type your message:\n").lower()

    shift = int(input("Type the shift number:\n"))

    caeser(text, shift, direction)

    restart = input("Do you wish to restart?: 'Yes' or 'No'\n").lower()
