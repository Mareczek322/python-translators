import os
os.system("cls")


def encode(message):
    msg = list(message)
    output = []

    for i in message:
        if i == "A":
            output.append("Alpha ")
        elif i == "B":
            output.append("Bravo ")
        elif i == "C":
            output.append("Charlie ")
        elif i == "D":
            output.append("Delta ")
        elif i == "E":
            output.append("Echo ")
        elif i == "F":
            output.append("Foxtrot ")
        elif i == "G":
            output.append("Golf ")
        elif i == "H":
            output.append("Hotel ")
        elif i == "I":
            output.append("India ")
        elif i == "J":
            output.append("Juliet ")
        elif i == "K":
            output.append("Kilo ")
        elif i == "L":
            output.append("Lima ")
        elif i == "M":
            output.append("Mike ")
        elif i == "N":
            output.append("November ")
        elif i == "O":
            output.append("Oscar ")
        elif i == "P":
            output.append("Papa ")
        elif i == "Q":
            output.append("Quebec ")
        elif i == "R":
            output.append("Romeo ")
        elif i == "S":
            output.append("Sierra ")
        elif i == "T":
            output.append("Tango ")
        elif i == "U":
            output.append("Uniform ")
        elif i == "V":
            output.append("Victor ")
        elif i == "W":
            output.append("Whiskey ")
        elif i == "X":
            output.append("X-ray ")
        elif i == "Y":
            output.append("Yankee ")
        elif i == "Z":
            output.append("Zulu ")
        elif i == " ":
            output.append(" /  ")
        else:
            output.append("")

    final = ''.join(output)
    print(final)
    input("Press enter to exit...")


def decode(message):
    msg = message.split(" ")
    output = []

    for i in msg:
        if i == "Alpha":
            output.append("A")
        elif i == "Bravo":
            output.append("B")
        elif i == "Charlie":
            output.append("C")
        elif i == "Delta":
            output.append("D")
        elif i == "Echo":
            output.append("E")
        elif i == "Foxtrot":
            output.append("F")
        elif i == "Golf":
            output.append("G")
        elif i == "Hotel":
            output.append("H")
        elif i == "India":
            output.append("I")
        elif i == "Juliet":
            output.append("J")
        elif i == "Kilo":
            output.append("K")
        elif i == "Lima":
            output.append("L")
        elif i == "Mike":
            output.append("M")
        elif i == "November":
            output.append("N")
        elif i == "Oscar":
            output.append("O")
        elif i == "Papa":
            output.append("P")
        elif i == "Quebec":
            output.append("Q")
        elif i == "Romeo":
            output.append("R")
        elif i == "Sierra":
            output.append("S")
        elif i == "Tango":
            output.append("T")
        elif i == "Uniform":
            output.append("U")
        elif i == "Victor":
            output.append("V")
        elif i == "Whiskey":
            output.append("W")
        elif i == "X-ray":
            output.append("X")
        elif i == "Yankee":
            output.append("Y")
        elif i == "Zulu":
            output.append("Z")
        elif i == "/":
            output.append(" ")
        else:
            output.append("")

    final = ''.join(output)
    print(final)
    input("Press enter to exit...")


def begin_phonetic():
    choice = input("Encode 1)\nDecode 2)\nChoice: ")
    if choice != "1" and choice != "2":
        begin_phonetic()
    elif choice == "1":
        message = input("What message would you like to encode? ").upper()
        encode(message)
    elif choice == "2":
        message = input("What message would you like to decode? ")
        decode(message)


if __name__ == "__main__":
    begin_phonetic()
