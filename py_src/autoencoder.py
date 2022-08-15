import torch
from torch.utils.data import Dataset
import pandas as pd
import numpy as np

class AutoEncoder(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.encoder_outer = torch.nn.Linear(16, 12)
        self.encoder_inner2 = torch.nn.Linear(12, 8)
        self.encoder_inner1 = torch.nn.Linear(8, 4)

        self.decoder_inner1 = torch.nn.Linear(4, 8)
        self.decoder_inner2 = torch.nn.Linear(8, 12)
        self.decoder_outer = torch.nn.Linear(12, 16)

    def forward(self, x):
        x = x / 16
        x = self.encoder_outer(x)
        x = self.encoder_inner2(x)
        x = self.encoder_inner1(x)
        x = self.decoder_inner1(x)
        x = self.decoder_inner2(x)
        x = self.decoder_outer(x)
        x = x * 16

        return x

# https://pytorch.org/tutorials/recipes/recipes/custom_dataset_transforms_loader.html
class CASDataset(Dataset):
    def __init__(self, file):
        self.df = pd.read_csv(file, delimiter=" ", header=None)
    
    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):
        return np.array(self.df.loc[idx]).astype(np.float32)

