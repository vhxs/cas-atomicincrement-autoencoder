unique = set()

for line in open("permutations.txt"):
    unique.add(line.strip())

print(len(unique))

# what if we drew all these interleavings as a Cayley graph?
# edges = transpositions
# neo4j?