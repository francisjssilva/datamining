import csv


def inputClassValue(message, maxCol):
    while True:
        try:
            userInput = int(input(message))
        except Exception:
            print("        Not a column number! Try again.")
            continue
        else:
            if userInput > maxCol:
                print("        Column nr. doesn't exist! Try again.")
                continue
            else:
                if userInput < 1:
                    print("        Column nr. must be greater than 0! Try again.")
                    continue
                else:
                    return userInput


def inputFloat(message):
    while True:
        try:
            userInput = float(input(message))
        except Exception:
            print("        Not a number! Try again.")
            continue
        else:
            if userInput > 1:
                print("        Ratio Must be lower than 1! Try again.")
                continue
            else:
                if userInput <= 0:
                    print("       Ratio Must be greater than 0! Try again.")
                    continue
                else:
                    return userInput


def inputPath(message):
    while True:
        try:
            userInput = raw_input(message)
            lines = csv.reader(open(userInput, "rb"))
            dataset = list(lines)
            maxCol = len(dataset[0]) - 1
        except Exception:
            print("        Fail to open it or file not found! Try again.")
            continue
        else:
            return userInput, maxCol


def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))
        except Exception:
            print("        Fail! Try again.")
            continue
        else:
            if userInput > 2:
                print("        Fail! Try again.")
                continue
            else:
                if userInput < 1:
                    print("        Fail! Try again.")
                    continue
                else:
                    return userInput


def clearScreen():
    clear = "\n" * 100
    print clear