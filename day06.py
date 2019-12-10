import base
import networkx as nx

filedata = base.file_to_string('input/day06.txt')

data = base.lmap(lambda x: x.split(')')[::-1], filedata.splitlines())
G = nx.DiGraph(data)

inodes = 0
for n in G.nodes():
    if G.out_degree(n) == 0:
        continue
    inodes += base.ilen(nx.bfs_successors(G, n))

print("res1", inodes)
print("res2", nx.shortest_path_length(G.to_undirected(), 'YOU', 'SAN')-2)
