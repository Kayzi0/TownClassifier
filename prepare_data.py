from ast import Str
import pandas as pd
import torch
import numpy as np
import pickle
#read csvs into pandas dataframes
cat = pd.read_csv(r"data\raw\cat.csv")
bal = pd.read_csv(r"data\raw\bal.csv")
val = pd.read_csv(r"data\raw\val.csv")
fr = pd.read_csv(r"data\raw\french-towns.csv")
cn = pd.read_csv(r"data\raw\chinese-towns.csv")
es = pd.read_csv(r"data\raw\spanish-towns-ex-cat.csv")

#add descriptor for row;
data = [cat, bal, val, fr, cn, es]
for dataset in data:
    dataset.columns = ["Town"]
    dataset["Town"] = dataset["Town"]

#modify set sizes to ensure even distribution

fr = fr[:int(fr.shape[0]/5)]
cn = cn[:int(cn.shape[0]/1.8)]

#concatenate catalan countries into one dataframe
cat = pd.concat([cat,val,bal])

#encode labels
labels = {"Catalan": 0, "French" : 1, "Chinese" : 2, "Spanish": 3}


#add labels
cat["Label"] = [labels["Catalan"] for i in range(cat.size)]
fr["Label"] = [labels["French"] for i in range(fr.size)]
cn["Label"] = [labels["Chinese"] for i in range(cn.size)]
es["Label"] = [labels["Spanish"] for i in range(es.size)]


data = pd.concat([cat, fr, cn, es])
#convert all towns to upper and lower case to double data
data_upper = data.applymap(lambda s: s.upper() if type(s) == str else s)
data_lower = data.applymap(lambda s: s.lower() if type(s) == str else s)
data = pd.concat([data_upper, data_lower])
def encodeStrings(data):
    #cast to list to allow string type conversion
    data = data.values.tolist()

    for pair in data:
        #convert strings to lists of characters
        pair[0] = list(pair[0])
        for i in range(len(pair[0])):
            #replace characters by unicode integer
            pair[0][i] = ord(pair[0][i])
    
    return data

data = encodeStrings(data)

def seperate_labels(data):
    #seperate data from labels
    data, labels = map(list, zip(*data))
    return data, labels

data, labels = seperate_labels(data)

#find longest word
max_string = max([len(i) for i in data])

#fill all other words with zeroes to match longest word
def fillWords(data, max_string):
    for word in data:
        while len(word) < max_string:
            word.append(0)
    return data

data = fillWords(data, max_string)

#shuffle arrays according to the same permutation
data = np.asarray(data)
labels = np.asarray(labels)
perm = np.random.permutation(data.shape[0])

data = data[perm]
labels = labels[perm]
slice1 = 0.8
slice2 = 0.95
train_data = data[:int((data.shape[0]*slice1))]
val_data = data[int((data.shape[0]*slice1)):int((data.shape[0]*slice2))]
test_data = data[int((data.shape[0]*slice2)):]
train_labels = labels[:int((labels.shape[0]*slice1))]
val_labels = labels[int((labels.shape[0]*slice1)):int((labels.shape[0]*slice2))]
test_labels = labels[int((labels.shape[0]*slice2)):]

pickle.dump(train_data, open(r"data\train_data.pkl", "wb"))
pickle.dump(val_data, open(r"data\val_data.pkl", "wb"))
pickle.dump(test_data, open(r"data\test_data.pkl", "wb"))
pickle.dump(train_labels, open(r"data\train_labels.pkl", "wb"))
pickle.dump(val_labels, open(r"data\val_labels.pkl", "wb"))
pickle.dump(test_labels, open(r"data\test_labels.pkl", "wb"))