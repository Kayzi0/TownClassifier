import pandas as pd
import torch
import numpy as np

#read csvs into pandas dataframes
cat = pd.read_csv(r"data\cat.csv")
bal = pd.read_csv(r"data\bal.csv")
val = pd.read_csv(r"data\val.csv")
fr = pd.read_csv(r"data\french-towns.csv")
de = pd.read_csv(r"data\german-towns.csv")
es = pd.read_csv(r"data\spanish-towns-ex-cat.csv")

#all descriptor for row
data = [cat, bal, val, fr, de, es]
for dataset in data:
    dataset.columns = ["Town"]

#concatenate catalan countries into one dataframe
cat = pd.concat([cat,val,bal])

#encode labels
labels = {"Catalan": 0, "French" : 1, "German" : 2, "Spanish": 3}


#add labels
cat["Label"] = [labels["Catalan"] for i in range(cat.size)]
fr["Label"] = [labels["French"] for i in range(fr.size)]
de["Label"] = [labels["German"] for i in range(de.size)]
es["Label"] = [labels["Spanish"] for i in range(es.size)]

data = [cat, fr, de, es]
#split into training, validation and test data
def get_train_n_test_data(data, slice1, slice2):
    train_data = pd.DataFrame(columns=["Town", "Label"])
    test_data = pd.DataFrame(columns=["Town", "Label"])
    val_data = pd.DataFrame(columns=["Town", "Label"])
    for dataset in data:
        train_data = pd.concat([train_data, dataset[:int(dataset.shape[0]*slice1)]])
        val_data = pd.concat([test_data, dataset[int(dataset.shape[0]*slice1):int(dataset.shape[0]*slice2)]])
        test_data = pd.concat([test_data, dataset[int(dataset.shape[0]*slice2):]])

    return train_data, val_data, test_data

train_data, val_data, test_data = get_train_n_test_data(data, 0.7, 0.9)

