import morse
import phonetic
import emoji
import os
os.system("cls")


def begin():
    choice = input("Morse Code 1)\nPhonetic Alphabet 2)\nEmojis 3)\nChoice: ")
    if choice != "1" and choice != "2" and choice != "3":
        begin()
    elif choice == "1":
        os.system("cls")
        morse.begin_morse()
    elif choice == "2":
        os.system("cls")
        phonetic.begin_phonetic()
    elif choice == "3":
        os.system("cls")
        emoji.begin_emoji()


begin()
