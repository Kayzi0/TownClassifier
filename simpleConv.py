import torch
from torch import nn
import torch.nn.functional as F

class simpleConv(nn.Module):
    def __init__(self):
        super().__init__()

        self.encoder = nn.Sequential (
            nn.Conv1d(1, 8, kernel_size=5, bias= False),
            #nn.BatchNorm1d(8),
            nn.ReLU(),

            nn.Conv1d(8,16, kernel_size=5, bias=False),
            #nn.BatchNorm1d(16),
            nn.ReLU(),

            nn.Conv1d(16, 32, kernel_size=5, bias=False),
            #nn.BatchNorm1d(32),
            nn.ReLU(),
        )

        self.avg_pool = nn.AdaptiveAvgPool1d(1)

        self.classifier = nn.Sequential(
            nn.Linear(32,8, bias=False),
            #nn.BatchNorm1d(8),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(8,4)
        )
    def forward(self, x):
        x = x.unsqueeze(dim=1)
        x = self.encoder(x)
        x = self.avg_pool(x)
        x = self.classifier(torch.flatten(x, start_dim=1))
        return x