from alphabet import alphabet


def decrypt(cipher_text, shift_amount):

    plain_text = ""

    for letter in cipher_text:

        if letter is ' ':
            plain_text += letter
            continue

        position = alphabet.index(letter)

        new_position = position - shift_amount

        plain_text += alphabet[new_position]

    print(f"The decoded text is {plain_text}")
