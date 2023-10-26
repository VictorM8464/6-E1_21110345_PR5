class DisjointSet:
    def __init__(self, vertices):
        self.parent = [-1] * vertices

    def union(self, root1, root2):
        if root1 != root2:
            self.parent[root1] = root2

    def find(self, vertex):
        if self.parent[vertex] == -1:
            return vertex
        return self.find(self.parent[vertex])

def kruskal(graph):
    num_vertices = len(graph)
    result = []
    edge_index = 0
    sorted_edges = sorted(
        [(graph[i][j], i, j) for i in range(num_vertices) for j in range(i + 1, num_vertices)]
    )
    disjoint_set = DisjointSet(num_vertices)

    while edge_index < num_vertices - 1:
        weight, src, dest = sorted_edges[edge_index]
        edge_index += 1
        root1 = disjoint_set.find(src)
        root2 = disjoint_set.find(dest)

        if root1 != root2:
            result.append((src, dest, weight))
            disjoint_set.union(root1, root2)

    return result

# Ejemplo de grafo ponderado en forma de matriz de adyacencia.
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0],
]

print("Pasos para construir el Arbol de Minimo Coste de Kruskal:")
minimum_spanning_tree = kruskal(graph)
for edge in minimum_spanning_tree:
    src, dest, weight = edge
    print(f"Arista: ({src}-{dest}) - Peso: {weight}")
