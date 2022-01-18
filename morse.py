import os
os.system("cls")


def encode(message):
    msg = list(message)
    output = []

    for i in message:
        if i == "A":
            output.append(".- ")
        elif i == "B":
            output.append("-... ")
        elif i == "C":
            output.append("-.-. ")
        elif i == "D":
            output.append("-.. ")
        elif i == "E":
            output.append(". ")
        elif i == "F":
            output.append("..-. ")
        elif i == "G":
            output.append("--. ")
        elif i == "H":
            output.append(".... ")
        elif i == "I":
            output.append(".. ")
        elif i == "J":
            output.append(".--- ")
        elif i == "K":
            output.append("-.- ")
        elif i == "L":
            output.append(".-.. ")
        elif i == "M":
            output.append("-- ")
        elif i == "N":
            output.append("-. ")
        elif i == "O":
            output.append("--- ")
        elif i == "P":
            output.append(".--. ")
        elif i == "Q":
            output.append("--.- ")
        elif i == "R":
            output.append(".-. ")
        elif i == "S":
            output.append("... ")
        elif i == "T":
            output.append("- ")
        elif i == "U":
            output.append("..- ")
        elif i == "V":
            output.append("...- ")
        elif i == "W":
            output.append(".-- ")
        elif i == "X":
            output.append("-..- ")
        elif i == "Y":
            output.append("-.-- ")
        elif i == "Z":
            output.append("--.. ")
        elif i == "1":
            output.append(".---- ")
        elif i == "2":
            output.append("..--- ")
        elif i == "3":
            output.append("...-- ")
        elif i == "4":
            output.append("....- ")
        elif i == "5":
            output.append("..... ")
        elif i == "6":
            output.append("-.... ")
        elif i == "7":
            output.append("--... ")
        elif i == "8":
            output.append("---.. ")
        elif i == "9":
            output.append("----. ")
        elif i == "0":
            output.append("----- ")
        elif i == ",":
            output.append("--..-- ")
        elif i == ".":
            output.append(".-.-.- ")
        elif i == "?":
            output.append("..--.. ")
        elif i == "!":
            output.append("..--. ")
        elif i == "\"":
            output.append(".-..-. ")
        elif i == ":":
            output.append("---... ")
        elif i == "'":
            output.append(".----. ")
        elif i == "-":
            output.append("-....- ")
        elif i == "/":
            output.append("-..-. ")
        elif i == "(":
            output.append("-.--. ")
        elif i == ")":
            output.append("-.--.- ")
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
        if i == ".-":
            output.append("A")
        elif i == "-...":
            output.append("B")
        elif i == "-.-.":
            output.append("C")
        elif i == "-..":
            output.append("D")
        elif i == ".":
            output.append("E")
        elif i == "..-.":
            output.append("F")
        elif i == "--.":
            output.append("G")
        elif i == "....":
            output.append("H")
        elif i == "..":
            output.append("I")
        elif i == ".---":
            output.append("J")
        elif i == "-.-":
            output.append("K")
        elif i == ".-..":
            output.append("L")
        elif i == "--":
            output.append("M")
        elif i == "-.":
            output.append("N")
        elif i == "---":
            output.append("O")
        elif i == ".--.":
            output.append("P")
        elif i == "--.-":
            output.append("Q")
        elif i == ".-.":
            output.append("R")
        elif i == "...":
            output.append("S")
        elif i == "-":
            output.append("T")
        elif i == "..-":
            output.append("U")
        elif i == "...-":
            output.append("V")
        elif i == ".--":
            output.append("W")
        elif i == "-..-":
            output.append("X")
        elif i == "-.--":
            output.append("Y")
        elif i == "--..":
            output.append("Z")
        elif i == ".---":
            output.append("1")
        elif i == "..---":
            output.append("2")
        elif i == "...--":
            output.append("3")
        elif i == "....-":
            output.append("4")
        elif i == ".....":
            output.append("5")
        elif i == "-....":
            output.append("6")
        elif i == "--...":
            output.append("7")
        elif i == "---..":
            output.append("8")
        elif i == "----.":
            output.append("9")
        elif i == "-----":
            output.append("0")
        elif i == "--..--":
            output.append(",")
        elif i == ".-.-.-":
            output.append(".")
        elif i == "..--..":
            output.append("?")
        elif i == "..--.":
            output.append("!")
        elif i == ".-..-.":
            output.append("\"")
        elif i == "---...":
            output.append(":")
        elif i == ".----.":
            output.append("'")
        elif i == "-....-":
            output.append("-")
        elif i == "-..-.":
            output.append("/")
        elif i == "-.--.":
            output.append("(")
        elif i == "-.--.-":
            output.append(")")
        elif i == "/":
            output.append(" ")
        else:
            output.append("")

    final = ''.join(output)
    print(final)
    input("Press enter to exit...")


def begin_morse():
    choice = input("Encode 1)\nDecode 2)\nChoice: ")
    if choice != "1" and choice != "2":
        begin_morse()
    elif choice == "1":
        message = input("What message would you like to encode? ").upper()
        encode(message)
    elif choice == "2":
        message = input("What message would you like to decode? ")
        decode(message)


if __name__ == "__main__":
    begin_morse()
