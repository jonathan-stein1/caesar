import sys, getopt

alph = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "p:f:o:", ["password=", "file=", "output="])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)

    if len(args) == 0:
        print("Usage: python caesar.py [options] [command] [message]")
        sys.exit(2)

    def getOpt(list):
        for option, value in opts:
            if option in list:
                return value

    if args[0] == "help":
        readme = open("README.txt", "r")
        print(readme.read())
        readme.close()

    if args[0] in ["encrypt", "decrypt"]:
        password = getOpt(["-p", "--password"])
        if password == None:
            print("You have to provide a password")
            sys.exit(2)

        file = getOpt(["-f", "--file"])
        input = None

        if file != None:
            inputFile = open(file, "r")
            input = inputFile.read()
            inputFile.close()

        else:
            if len(args) < 2:
                print("You have to provide a message")
                sys.exit(2)

            else:
                input = args[1]

        text = None

        if args[0] == "encrypt":
            text = encrypt(input, password)

        else: # args[0] == "decrypt"
            text = decrypt(input, password)

        output = getOpt(["-o", "--output"])
        if output != None:
            outputFile = open(output, "w")
            outputFile.write(text)
            outputFile.close()

        else:
            print(text)

    else:
        print("Unknown command: " + args[0])
        sys.exit(2)

def encrypt(message, password):
    convertedPassword = convertPassword(password)
    out = ""

    for char in message:
        index = len(out) % len(convertedPassword)
        count = convertedPassword[index]
        newChar = increaseBy(char, count)

        out += newChar

    return out

def decrypt(message, password):
    convertedPassword = convertPassword(password)
    out = ""

    for char in message:
        index = len(out) % len(convertedPassword)
        count = convertedPassword[index]
        newChar = decreaseBy(char, count)

        out += newChar

    return out

def convertPassword(password):
    outList = []

    for char in password:
        if char.lower() in alph:
            index = alph.index(char.lower())

            outList.append(index + 1)

        elif char.isdigit():
            outList.append(int(char))

        else:
            outList.append(0)

    return outList

def increaseBy(char, count):
    newChar = None

    if char.lower() in alph:
        if char.isupper():
            upper = True

        else:
            upper = False

        charIndex = alph.index(char.lower())
        newIndex = (charIndex + count) % len(alph)
        newChar = alph[newIndex]

        if upper:
            newChar = newChar.upper()

    elif char.isdigit():
        digit = int(char)
        newDigit = (digit + count) % 10
        newChar = str(digit)

    else:
        newChar = char

    return newChar

def decreaseBy(char, count):
    newCount = count * -1

    return increaseBy(char, newCount)

if __name__ == "__main__":
    main()
