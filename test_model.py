import torch
from py_src.autoencoder import AutoEncoder
from subprocess import run, PIPE
import numpy as np
from random import shuffle, random
from statistics import harmonic_mean
import matplotlib.pyplot as plt

model = AutoEncoder()
model.load_state_dict(torch.load("autoencoder"))
model.eval()

# return confusion matrix
def test_model(threshold):
    trials = 2_000

    tp = 0
    tn = 0
    fp = 0
    fn = 0
    for k in range(trials):
        flip = random()

        # real data
        if flip > 0.5:
            real = True
            proc = run(["./main"], stdout=PIPE)
            permutation = torch.Tensor([int(n) for n in proc.stdout.decode("utf8").split()])
            output = model(permutation).tolist()

            permutation = np.array(permutation)
            output = np.array([round(o) for o in output])
        
        # fake
        else:
            real = False
            permutation = list(range(16))
            shuffle(permutation)
            permutation = torch.Tensor(permutation)
            output = model(permutation).tolist()

            permutation = np.array(permutation)
            output = np.array([round(o) for o in output])

        error = np.linalg.norm(permutation - output, ord=1)
        pred_real = (error < threshold)

        if real and pred_real:
            tp += 1
        elif real and not pred_real:
            fn += 1
        elif not real and pred_real:
            fp += 1
        else:
            tn += 1

    return tp, tn, fp, fn

x_data = []
y_data = []
for threshold in range(35, 70):
    tp, tn, fp, fn = test_model(threshold)

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    fallout = fp / (fp + tn)

    print(f"Threshold: {threshold}")
    print(f"FPR: {fallout}")
    print(f"TPR: {recall}")
    print()

    x_data.append(fallout)
    y_data.append(recall)

plt.xlim([0, 1])
plt.ylim([0, 1])
plt.plot(x_data, y_data)
plt.show()