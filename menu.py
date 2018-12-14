import bayes
import c45
import verifications


def mainMenu():
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("|||                                                           |||")
    print("|||             XICO'S DATA MINING PREDICTION APP             |||")
    print("|||                                                           |||")
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("|||                                                           |||")
    print("|||                      CHOOSE ALGORITHM                     |||")
    print("|||                                                           |||")
    print("|||       1. NAIVE BAYES                                      |||")
    print("|||       2. C4.5                                             |||")
    print("|||                                                           |||")
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

    inputChoosen = verifications.inputNumber("\n        Input: ")
    print"        Choosen:", inputChoosen
    verifications.clearScreen()

    if inputChoosen == 1:
        datasetPath, maxCol = dataSetPathMenu()
        classValue = classValueMenu(maxCol)
        spliRatio = sRatioMenu()
        print('datasetPath: {0} \nclassValue: {1} \nspliRatio: {2} \nmaxCol: {3}', datasetPath, classValue, spliRatio, maxCol)
        bayes.naiveBayesHandler(datasetPath, classValue, spliRatio)
        return 0

    if inputChoosen == 2:
        c45.c45Handler()

    return 0


def sRatioMenu():
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("|||                                                           |||")
    print("|||              INSERT SPLIT RATIO IN ORDER TO               |||")
    print("|||               SPLIT TRAIN SET AND TEST SET                |||")
    print("|||                     (BETWEEN 0 AND 1)                     |||")
    print("|||                                                           |||")
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    inputChoosen = verifications.inputFloat("\n        Split Ratio: ")
    print"        Choosen:", inputChoosen
    verifications.clearScreen()

    return inputChoosen


def classValueMenu(maxCol):
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("|||                                                           |||")
    print("|||                 INSERT CLASS VALUE COLUMN                 |||")
    print("|||                     (CLASS TO PREDICT)                    |||")
    print("|||                                                           |||")
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    inputChoosen = verifications.inputClassValue("\n        Column Nr.: ", maxCol)
    print"        Choosen:", inputChoosen
    verifications.clearScreen()

    return inputChoosen


def dataSetPathMenu():
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("|||                                                           |||")
    print("|||                   INSERT DATA SET PATH                    |||")
    print("|||                      (USING \"/\")                        |||")
    print("|||                                                           |||")
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    inputChoosen, maxColNr = verifications.inputPath("\n        Dataset Path: ")
    print"        Choosen:", inputChoosen
    verifications.clearScreen()

    return inputChoosen, maxColNr
