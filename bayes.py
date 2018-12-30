import csv
import numpy as np
import random
import math

from sklearn.metrics import confusion_matrix, classification_report, accuracy_score


def loadCsv(filename):
    lines = csv.reader(open(filename, "rb"))
    dataset = list(lines)
    for i in range(len(dataset)):
        dataset[i] = [float(x) for x in dataset[i]]
    return dataset


def splitDataset(dataset, splitRatio):
    trainSize = int(len(dataset) * splitRatio)
    trainSet = []
    copy = list(dataset)
    while len(trainSet) < trainSize:
        index = random.randrange(len(copy))
        trainSet.append(copy.pop(index))
    return [trainSet, copy]


def separateByAttribute(dataset, classValue):
    sepAtt = {}
    for i in range(len(dataset)):
        vector = dataset[i]
        if vector[classValue] not in sepAtt:
            sepAtt[vector[classValue]] = []
        sepAtt[vector[classValue]].append(vector)
    return sepAtt


def average(attributeValues):
    return sum(attributeValues) / float(len(attributeValues))


def standardDeviation(attributeValues):
    avg = average(attributeValues)
    variance = sum([pow(x - avg, 2) for x in attributeValues]) / float(len(attributeValues) - 1)
    return math.sqrt(variance)


def summarize(dataset, classValue):
    separated = separateByAttribute(dataset, classValue)
    summaries = {}
    for clVal, instances in separated.iteritems():
        summar = [(average(attribute), standardDeviation(attribute)) for attribute in zip(*instances)]
        del summar[classValue]
        summaries[clVal] = summar
    return summaries


def calculateProbability(x, mean, stdev):
    exponent = math.exp(-(math.pow(x - mean, 2) / (2 * math.pow(stdev, 2))))
    return (1 / (math.sqrt(2 * math.pi) * stdev)) * exponent


def calculateClassProbabilities(summaries, inputVector):
    probabilities = {}
    for classValue, classSummaries in summaries.items():
        probabilities[classValue] = 1
        for i in range(len(classSummaries)):
            mean, stdev = classSummaries[i]
            x = inputVector[i]
            probabilities[classValue] *= calculateProbability(x, mean, stdev)
    return probabilities


def predict(summaries, inputVector):
    probabilities = calculateClassProbabilities(summaries, inputVector)
    bestLabel, bestProb = None, -1
    for classValue, probability in probabilities.items():
        if bestLabel is None or probability > bestProb:
            bestProb = probability
            bestLabel = classValue
    return bestLabel


def getPredictions(summaries, testSet):
    predictions = []
    for i in range(len(testSet)):
        result = predict(summaries, testSet[i])
        predictions.append(result)
    return predictions


def getAccuracy(testSet, predictions):
    correct = 0
    for i in range(len(testSet)):
        if testSet[i][-1] == predictions[i]:
            correct += 1
    return (correct / float(len(testSet))) * 100.0


"""
    0 => fixed acidity
    1 => volatile acidity
    2 => citric acid,residual sugar
    3 => chlorides
    4 => free sulfur dioxide
    5 => total sulfur dioxide
    6 => density
    7 => pH
    8 => sulphates
    9 => alcohol
    10 => quality
"""


def naiveBayesHandler(dataset, classValue, splitRatio):
    # datasets/winequalityTest.csv
    dataset = loadCsv(dataset)

    print '\nFile {0} was read succesfully with {1} rows\n'.format('winequality-red', len(dataset))
    print '\nSpliting Dataset... It may take some time... It will depend on Dataset size.\n'

    # Split in training set and test set using a splitRatio
    trainSet, testSet = splitDataset(dataset, splitRatio)
    print 'Dataset was successfully splitted into {0}% Train Set and {1}% Test Set!\n'.format(abs(splitRatio*100), abs(100-(splitRatio*100)))
    # print '\nSplit {0} rows into train with {1} and test with {2}'.format(len(dataset), trainSet, testSet)

    # Separate by attribute the train data set
    summary = summarize(trainSet, classValue)
    # print '\nSummary by class value: \n{0}'.format(summary)

    # Predict
    predictions = getPredictions(summary, testSet)

    testValues = np.delete(testSet, np.s_[:classValue:], 1)

    print(confusion_matrix(testValues, predictions))
    print(classification_report(testValues, predictions))
    print("Accuracy: {0}%".format(accuracy_score(testValues, predictions)*100))

    return 0
