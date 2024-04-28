alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
#
# def encrypt(plain_text, shift_amount):
#   cipher_text = ""
#   for letter in plain_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount
#     cipher_text += alphabet[new_position]
#   print(f"The encoded text is {cipher_text}")
#
# def decrypt(cipher_text, shift_amount):
#   plain_text = ""
#   for letter in cipher_text:
#     position = alphabet.index(letter)
#     new_position = position - shift_amount
#     plain_text += alphabet[new_position]
#   print(f"The decoded text is {plain_text}")
#
# if direction == "encode":
#   encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#   decrypt(cipher_text=text, shift_amount=shift)
def ceasar(direction_input, text_input, shift_number):
    if direction_input == 'encode':
        encrypted = ""
        for letter in text_input:
            position = alphabet.index(letter)
            new_position = position + shift_number
            encrypted += alphabet[new_position]
        print(f"The encrypted message is {encrypted}.")
    elif direction_input == 'decode':
        decrypt = ""
        for letter in text_input:
            position = alphabet.index(letter)
            new_position = position - shift_number
            decrypt += alphabet[new_position]
        print(f"The decrypted message is {decrypt}.")
    else:
        print('Enter either encode or decode')
ceasar(direction, text, shift)



#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
ceasar(direction, text, shift)