import torch
import numpy as np
from torch.utils.data import Dataset, DataLoader

class TownsDataset(Dataset):
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels
    
    def __len__(self):
        return len(self.data)
        

    def __getitem__(self, idx):
        return self.data[idx], self.labels[idx]