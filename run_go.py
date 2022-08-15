from subprocess import run, PIPE
import pickle

trials = 100_000
permutation_list = []

# i is in the jth position distributions[i][j] times
distributions = {i: {j: 0 for j in range(16)} for i in range(16)}

for k in range(trials):
    print(k)
    proc = run(["./main"], stdout=PIPE)
    permutation = [int(n) for n in proc.stdout.decode("utf8").split()]
    
    for i, n in enumerate(permutation):
        distributions[n][i] += 1

    permutation_list.append(permutation)

training_data = open("permutations.txt", "w")
for permutation in permutation_list:
    training_data.write(" ".join(str(n) for n in permutation) + "\n")
training_data.close()

pickle.dump(distributions, open("distributions.pickle", "wb"))