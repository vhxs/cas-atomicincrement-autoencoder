from importlib.metadata import distribution
import pickle
import matplotlib.pyplot as plt

distributions = pickle.load(open("distributions.pickle", "rb"))
for k in distributions:
    bars = [distributions[k][i] for i in range(16)]
    print(max([(val, idx) for idx, val in enumerate(bars)])[1])
    plt.bar(range(16), bars)
    plt.title(k)
    plt.show()