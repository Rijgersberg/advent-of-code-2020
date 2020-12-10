from collections import defaultdict, Counter
import networkx as nx

from aoc import get_input

adapters = sorted([int(line) for line in get_input(day=10)])
device = adapters[-1] + 3
outlet = 0

# 10-1
sequence = [outlet] + adapters + [device]
jumps = [next_adap - prev_adap for next_adap, prev_adap in zip(sequence[1:], sequence[:-1])]

counts = Counter(jumps)
print(counts[1] * counts[3])

# 10-2
G = nx.DiGraph()
sequence_set = set(sequence)
for adapter in sequence:
    for i in range(1, 3 + 1):
        if adapter + i in sequence_set:
            G.add_edge(adapter, adapter + i)

n_paths = defaultdict(int)
n_paths[device] = 1
for n in list(nx.algorithms.dag.topological_sort(G))[::-1]:
    for parent, _ in G.in_edges(n):
        n_paths[parent] += n_paths[n]

print(n_paths[outlet])
