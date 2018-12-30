#!/usr/bin/env python
import csv
import numpy as np

from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


def loadCsv(filename):
    lines = csv.reader(open(filename, "rb"))
    dataset = list(lines)
    for i in range(len(dataset)):
        dataset[i] = [float(x) for x in dataset[i]]
    return dataset


def aggregate(list):
    newList = []
    for i in list:
        for j in i:
            newList.append(j)
    return newList


def c45Handler(dataset, classValue, splitRatio):
    dataset = loadCsv(dataset)

    print '\nFile {0} was read succesfully with {1} rows'.format('winequality-red', len(dataset))
    print '\nSpliting Dataset... It may take some time... It will depend on Dataset size.'

    X = np.delete(dataset, np.s_[classValue], 1)
    Y = np.delete(dataset, np.s_[:classValue:], 1)
    Y = aggregate(Y)

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=1 - splitRatio)
    print 'Dataset was successfully splitted into {0}% Train Set and {1}% Test Set!'.format(abs(splitRatio*100), abs(100-(splitRatio*100)))

    classifier = DecisionTreeClassifier()
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)

    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))
    print("Accuracy: {0}%".format(accuracy_score(y_test, y_pred)*100))
    return 0
