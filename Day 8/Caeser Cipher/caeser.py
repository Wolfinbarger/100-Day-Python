from alphabet import alphabet


def caeser(start_text, shift_amount, cipher_direction):

    end_text = ""

    if cipher_direction == "decode":
        shift_amount *= -1

    for letter in start_text:

        if letter is ' ':
            cipher_text += letter
            continue

        position = alphabet.index(letter)

        new_position = position + shift_amount

        end_text += alphabet[new_position]

    print("The {cipher_direction}d text is {end_text}")
