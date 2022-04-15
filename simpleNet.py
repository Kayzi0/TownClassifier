from turtle import forward
import torch
from torch import dropout, nn
import torch.nn.functional as F

class simpleNet(nn.Module):
    def __init__(self):
        super().__init__()

        self.layer = nn.Sequential(        
            nn.Linear(10,20),
            nn.BatchNorm1d(20),
            nn.Dropout(0.1),
            nn.Linear(20,40),
            nn.BatchNorm1d(40),
            nn.Dropout(0.1),
            nn.ReLU(),
            nn.Linear(40, 20),
            nn.BatchNorm1d(20),
            nn.Dropout(0.1),
            nn.Linear(20, 8),
            nn.BatchNorm1d(8),
            nn.Dropout(0.1),  
            nn.ReLU(),
            nn.Linear(8,4)
        )

    def forward(self, x):
        x = self.layer(x)
        return x