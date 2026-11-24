from sys import stdin

amount_vertexes, amount_edges = map(int, stdin.readline().split())

adjacency_matrix = [[0 for _ in range(amount_vertexes)] for _ in range(amount_vertexes)]

for _ in range(amount_edges):
    ind_ver_1, ind_ver_2 = map(int, stdin.readline().split())
    adjacency_matrix[ind_ver_1 - 1][ind_ver_2 - 1] = 1
    adjacency_matrix[ind_ver_2 - 1][ind_ver_1 - 1] = 1

bool_full_graph = True

for vertex_out in adjacency_matrix:
    if((amount_vertexes - 1) > sum(vertex_out)):
        bool_full_graph = False
        break

if(bool_full_graph):
    print("YES")
else:
    print("NO")
