import numpy as np

def decodeTown(town):
    town = town[town != 0]
    town = list(town)
    for i in range(len(town)):
        town[i] = chr(town[i])
    town = "".join(town)
    return town



def decodeLabels(label):
    labels = {0: "Catalan", 1: "French", 2: "Chinese", 3 : "Spanish"}
    return labels[label]
