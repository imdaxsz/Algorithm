parent = dict()
rank = dict()

def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1

def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0

def kruskal(graph):
    for vertice in graph['vertices']:
        make_set(vertice)
    minimum_spanning_tree = set()
    edges = list(graph['edges'])
    edges.sort()

    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.add(edge)
    return sorted(minimum_spanning_tree)


graph = {
'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
'edges': set([
(7, 'A', 'B'),
(7, 'B', 'A'),
(5, 'A', 'D'),
(5, 'D', 'A'),
(10, 'A', 'H'),
(10, 'H', 'A'),
(8, 'B', 'C'),
(8, 'C', 'B'),
(9, 'B', 'H'),
(9, 'H', 'B'),
(6, 'B', 'E'),
(6, 'E', 'B'),
(4, 'B', 'D'),
(4, 'D', 'B'),
(3, 'C', 'E'),
(3, 'E', 'C'),
(2, 'C', 'H'),
(2, 'H', 'C'),
(11, 'C', 'I'),
(11, 'I', 'C'),
(5, 'C', 'F'),
(5, 'F', 'C'),
(7, 'D', 'E'),
(7, 'E', 'D'),
(8, 'E', 'F'),
(8, 'F', 'E'),
(9, 'E', 'J'),
(9, 'J', 'E'),
(11, 'F', 'G'),
(11, 'G', 'F'),
(10, 'F', 'J'),
(10, 'J', 'F'),
(3, 'F', 'I'),
(3, 'I', 'F'),
(4, 'G', 'J'),
(4, 'J', 'G'),
(9, 'G', 'I'),
(9, 'I', 'G'),
(12, 'H', 'I'),
(12, 'I', 'H'),
])}

print(kruskal(graph))