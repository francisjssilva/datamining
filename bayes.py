import csv
import random
import math


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


def summarizeByClass(dataset, classValue):
    separated = separateByAttribute(dataset, classValue)
    summaries = {}
    for clval, attributeByClassValues in separated.iteritems():
        summaries = [(average(attributeValues), standardDeviation(attributeValues)) for attributeValues in zip(*attributeByClassValues)]
        del summaries[-1]
        summaries[int(clval)] = summaries
    return summaries


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
    dataset = loadCsv(dataset)

    print('\nFile {0} was read succesfully with {1} rows').format('winequality-red', len(dataset))
    print('\nSpliting Dataset... It may take some time...')

    trainSet, testSet = splitDataset(dataset, splitRatio)
    print('\nSplit {0} rows into train with {1} and test with {2}').format(len(dataset), trainSet, testSet)

    separated = separateByAttribute(dataset, classValue)
    print('\n\n\nSeparated instances: \n{0}').format(separated)

    summarizeByClass(dataset, classValue)
    summary = summarizeByClass(dataset, classValue)
    print('\nSummary by class value: \n{0}').format(summary)

    return 0
