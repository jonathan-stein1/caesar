import sys, getopt

alph = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:o:", ["input=", "output="])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)

    def getOpt(list):
        for option, value in opts:
            if option in list:
                return value

    input = getOpt(["-i", "--input"])
    output = getOpt(["-o", "--output"])

    print(reconstruct(input, output))

def reconstruct(input, output):
    return getSmallest(fillAllIn(checkRepeats(reconstructRaw(input, output))))

def reconstructRaw(input, output):
    password = ""

    for i in range(len(output)):
        x = input[i].lower()
        y = output[i].lower()

        if x in alph:
            indexX = alph.index(x)
            indexY = alph.index(y)

            if indexX == indexY:
                password += "-"

            else:
                password += alph[indexY - indexX - 1]

        else:
            password += "?"

    return password

def checkRepeats(password):
    passwords = []

    for i in range(1, len(password)):
        passwords1 = splitBy(password, i)
        if compareList(passwords1):
            passwords.append(passwords1)

    if len(passwords) == 0:
        return [[password]]

    else:
        return passwords

def compareList(list):
    for str1 in list:
        for str2 in list:
            if not compare(str1, str2):
                return False

    return True

def compare(str1, str2):
    for i in range(len(str1)):
        if i == len(str2):
            return True

        if str1[i] != str2[i] and str1[i] != "?" and str2[i] != "?":
            return False

    return True

def fillIn(passwords):
    password = ""

    length = len(passwords[0])

    for i in range(length):
        password += getCharAt(passwords, i)

    return password

def fillAllIn(passwordsList):
    passwords = []

    for passwords1 in passwordsList:
        passwords.append(fillIn(passwords1))

    return passwords

def getCharAt(list, index):
    for str in list:
        if index >= len(str):
            continue

        elif str[index] != "?":
            return str[index]

    return "?"

def splitBy(str, count):
    list = []

    for i in range(0, len(str), count):
        list.append(str[i:i + count])

    return list

def getSmallest(passwordList):
    longest = passwordList[len(passwordList) - 1]

    for password in passwordList:
        if fitsIn(password, longest):
            return password

    return longest

def fitsIn(str1, str2):
    for i in range(len(str2)):
        index1 = i % len(str1)

        if str1[index1] != str2[i] and str1[index1] != "?" and str2[i] != "?":
            return False

    return True

def convertPassword(password):
    newPassword = ""

    for char in password.lower():
        if char in alph and char != "z":
            newPassword += char

        else:
            newPassword += "-"

    return newPassword

if __name__ == "__main__":
    main()
