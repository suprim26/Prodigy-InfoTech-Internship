#Ceasar Cipher encryption and decryption of alphabets and numericals
def encryption(plain_text, shift_key):
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():  # Check if character is a letter
            alphabet = 'abcdefghijklmnopqrstuvwxyz'
            if char.isupper():  # Check if character is uppercase
                alphabet = alphabet.upper()
            position = alphabet.index(char.lower())
            new_position = (position + shift_key) % 26
            cipher_text += alphabet[new_position]
        elif char.isdigit():  # Check if character is a digit
            new_digit = (int(char) + shift_key) % 10
            cipher_text += str(new_digit)
        else:  # Character is a special character
            cipher_text += char
    print(f"Here's the text after encryption: {cipher_text}")


def decryption(cipher_text, shift_key):
    plain_text = ""
    for char in cipher_text:
        if char.isalpha():  # Check if character is a letter
            alphabet = 'abcdefghijklmnopqrstuvwxyz'
            if char.isupper():  # Check if character is uppercase
                new_char = chr((ord(char) - 65 - shift_key) % 26 + 65)
            else:
                new_char = chr((ord(char) - 97 - shift_key) % 26 + 97)
            plain_text += new_char
        elif char.isdigit():  # Check if character is a digit
            new_digit = (int(char) - shift_key) % 10
            plain_text += str(new_digit)
        else:  # Character is a special character
            plain_text += char

    print(f"Here's the text after decryption: {plain_text}")
    
bye_bye=False
while not bye_bye:
    what_to_do = input("Type 'encrypt' for encryption, type 'decrypt' for decryption:\n")
    text = input("Type your Message:\n")
    shift = int(input("Enter the shift key:\n"))
    if what_to_do == "encrypt":
        encryption(text, shift)
    elif what_to_do == "decrypt":
        decryption(text, shift)
    repeat=input("Type 'yes' to continue, type 'no' to exit:\n")
    if repeat=='no':
        bye_bye=True
        print("Have a Good Day!")