from sys import stdin

amount_vertexes, amount_edges = map(int, stdin.readline().split())

adjacency_matrix = [[0 for _ in range(amount_vertexes)] for _ in range(amount_vertexes)]

for _ in range(amount_edges):
    vertex_1, vertex_2 = map(int, stdin.readline().split())
    adjacency_matrix[vertex_1 - 1][vertex_2 - 1] = 1

for stroke in adjacency_matrix:
    print(" ".join(map(str, stroke)))