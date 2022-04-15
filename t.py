from TownsDataset import TownsDataset
from simpleNet import simpleNet
import torch
from torch.utils.data import DataLoader
import numpy as np
import pickle
from matplotlib import pyplot as plt

train_data = pickle.load(open(r"data\train_data.pkl", "rb"))
train_labels = pickle.load(open(r"data\train_labels.pkl", "rb"))
val_data = pickle.load(open(r"data\val_data.pkl", "rb"))
val_labels = pickle.load(open(r"data\val_labels.pkl", "rb"))


train_dl = DataLoader(dataset=TownsDataset(train_data, train_labels), batch_size=32)
val_dl = DataLoader(dataset=TownsDataset(val_data, val_labels), batch_size=64)


train_label_count = TownsDataset(train_data, train_labels).num_labels
print(train_label_count)