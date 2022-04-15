from turtle import forward
import torch
from torch import nn
import torch.nn.functional as F

class simpleNet(nn.Module):
    def __init__(self):
        super().__init__()

        self.layer = nn.Sequential(        
            nn.Linear(37,64),
            nn.BatchNorm1d(64),
            nn.ReLU(),
            nn.Linear(64,32),
            nn.BatchNorm1d(32),
            nn.ReLU(),
            nn.Linear(32,8),
            nn.BatchNorm1d(8),
            nn.ReLU(),
            nn.Linear(8,4)
        )

    def forward(self, x):
        x = self.layer(x)
        x = F.softmax(x)
        return x