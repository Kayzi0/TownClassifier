from turtle import forward
import torch
from torch import nn
import torch.nn.functional as F

class simpleNet(nn.Module):
    def __init__(self, c_in, c_out):
        super().__init__()

        self.layer = nn.Sequential(
            nn.Linear(8,16),
            nn.BatchNorm1d(16),
            nn.ReLU(),
            nn.Linear(16,8),
            nn.BatchNorm1d(8),
            nn.ReLU(),
            nn.Linear(8,4)
        )

    def forward(self, x):
        x = self.layer(x)
        x = F.softmax(x)
        return x