import torch
from torch.utils.data import DataLoader
from py_src.autoencoder import AutoEncoder, CASDataset

dataset = CASDataset("permutations.txt")
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)
model = AutoEncoder()

optimizer = torch.optim.Adam(model.parameters(), lr=0.0001)
criterion = torch.nn.L1Loss()

for epoch in range(5):
    running_loss = 0

    for i, seq in enumerate(dataloader):
        optimizer.zero_grad()

        output = model(seq)
        loss = criterion(output, seq)
        loss.backward()
        optimizer.step()

        # print statistics
        running_loss += loss.item()
        if i % 200 == 199:    # print every 200 mini-batches
            print(f'[{epoch + 1}, {i + 1:5d}] loss: {running_loss / 200:.3f}')
            running_loss = 0.0

print('Finished Training')

torch.save(model.state_dict(), "autoencoder")