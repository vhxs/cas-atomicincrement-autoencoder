import torch
from py_src.autoencoder import AutoEncoder

model = AutoEncoder()
model.load_state_dict(torch.load("autoencoder"))
model.eval()

while True:
    try:
        test_input = input("Test input: ")
        test_input = test_input.strip().split()
        test_input = torch.Tensor([int(x) for x in test_input])

        output = model(test_input)
        output = output.detach().numpy()
        output = [str(round(o)) for o in output]
        output = " ".join(output)

        print(output)

    except KeyboardInterrupt:
        print("Exiting")
        exit()