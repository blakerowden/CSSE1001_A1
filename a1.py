#!/usr/bin/env python3
"""
Assignment 1
CSSE1001/7030
Semester 2, 2018
"""

from a1_support import is_word_english

__author__ = "Blake Rowden s4427634"


ALPHABET = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"


def encrypt(text, offset):
    """Encrypts text by replacing each letter with the letter some fixed number
     of positions (the offset) down the alphabet. Returns the encrypted text.

    Parameters:
        text (str): Text to encrypt
        offset (int): Number to offset each character

    Return:
        str: Final encrypted text

    Preconditions:
        0 < offset < 26 for encryption OR offset = 0 for all encryptions
    """
    encryption = ""
    for char in text:  # Character moved forward every second index to preserve capitalisation
        if char in ALPHABET:
            encryption += ALPHABET[(ALPHABET.index(char) + offset*2) % len(ALPHABET)]
        else:
            encryption += char
    return encryption


def decrypt(text, offset):
    """Decrypts text that was previously encrypted by the encrypt function. Returns the decrypted text.
    However, if normal text is cycled through it will simply place a negative decryption on the string.

    Parameters:
        text (str): text to decrypt
        offset (int): Number original text was offset

    Return:
        str: original text decrypted

    Preconditions:
        0 < offset < 26 for decryption OR offset = 0 for all decryptions
    """
    decryption = ""
    for char in text:  # Character moved backward every second index to preserve capitalisation
        if char in ALPHABET:
            decryption += ALPHABET[(ALPHABET.index(char) - offset*2) % len(ALPHABET)]
        else:
            decryption += char
    return decryption


def find_encryption_offsets(encrypted_text):
    """Returns a tuple containing all possible offsets that could have been used if to encrypt
    some English text

    Parameters:
        encrypted_text: (str) The string to test for possible offsets

    Return:
        tuple: list if integers that could be the offset
    """
    possible_offset = ()
    for o in range(26):
        offset_test = decrypt(encrypted_text.lower(), o)
        eng_test = False
        for word in offset_test.split():

            # Splits words containing '-' into two separate words and checks them individually
            if '-' in word:
                for word_a_b in word.split("-"):
                    temp_word = ""
                    for char in word_a_b:
                        if char in ALPHABET:
                            temp_word = temp_word + char
                    if not is_word_english(temp_word):
                        eng_test = True

            # Runs check for a single word
            else:
                temp_word = ""
                for char in word:
                    if char in ALPHABET:
                        temp_word = temp_word + char
                if not is_word_english(temp_word):
                    eng_test = True

        if not eng_test:
            possible_offset += (o,)

    return possible_offset


def main():
    """
    Main console script will run from here
    All UI code is below
    """
    print("Welcome to the simple encryption tool!\n")

    user_active = True
   
    while user_active:
        print("Please choose an option [e/d/a/q]:\n"
              "  e) Encrypt some text\n"
              "  d) Decrypt some text\n"
              "  a) Automatically decrypt English text\n"
              "  q) Quit")
        user_choice = input("> ")

        if user_choice == "q":
            print("Bye!")
            user_active = False

        elif user_choice == "e":
            text = str(input("Please enter some text to encrypt: "))
            offset = input("Please enter a shift offset (1-25): ")
            if offset == "0":
                print("The encrypted text is:")
                for o in range(1, 26):
                    print("  " + str(o).zfill(2) + ": " + encrypt(text, o))  # Cycle through every encrypt possibility
                print("")
            else:
                print("The encrypted text is: " + encrypt(text, int(offset)) + "\n")

        elif user_choice == "d":
            text = str(input("Please enter some text to decrypt: "))
            offset = input("Please enter a shift offset (1-25): ")
            if offset == "0":
                for o in range(1, 26):
                    print("  " + str(o).zfill(2) + ": " + decrypt(text, o))
                print("")
            else:
                print("The decrypted text is: " + decrypt(text, int(offset)) + "\n")

        elif user_choice == "a":
            text = str(input("Please enter some encrypted text: "))
            offset_list = find_encryption_offsets(text)
            if len(offset_list) == 0:
                print("No valid encryption offset\n")
            elif len(offset_list) > 1:
                print("Multiple encryption offsets: " + ", ".join(str(x) for x in offset_list) + "\n")
            else:  # If only 1 possible offset print the decryption
                print("Encryption offset: " + str(offset_list[0]))
                print("Decrypted message: " + decrypt(text, int(offset_list[0])) + "\n")

        else:
            print("Invalid command\n")


##################################################
# !! Do not change (or add to) the code below !! #
#
# This code will run the main function if you use
# Run -> Run Module  (F5)
# Because of this, a "stub" definition has been
# supplied for main above so that you won't get a
# NameError when you are writing and testing your
# other functions. When you are ready please
# change the definition of main above.
###################################################

if __name__ == '__main__':
    main()

