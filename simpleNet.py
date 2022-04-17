import torch
from torch import nn
import torch.nn.functional as F

class simpleNet(nn.Module):
    def __init__(self):
        super().__init__()

        self.layer = nn.Sequential(        
            nn.Linear(36,64),
            #nn.BatchNorm1d(64),
            nn.Dropout(0.2),
            nn.Linear(64,32),
            #nn.BatchNorm1d(32),
            nn.Dropout(0.2),
            nn.ReLU(),
            nn.Linear(32, 16),
            #nn.BatchNorm1d(16),
            nn.Dropout(0.2),
            nn.Linear(16, 8),
            #nn.BatchNorm1d(8),
            nn.Dropout(0.2),  
            nn.ReLU(),
            nn.Linear(8,4)
        )

    def forward(self, x):
        x = self.layer(x)
        return x