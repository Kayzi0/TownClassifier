import numpy as np

def decodeTown(town):
    town = town[town != 0]
    town = list(town)
    for i in range(len(town)):
        town[i] = chr(town[i])
    town = "".join(town)
    return town



def decodeLabels(label):
    labels = {0: "French", 1: "Chinese"}
    return labels[label]
