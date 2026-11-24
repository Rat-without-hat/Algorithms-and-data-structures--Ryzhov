from sys import stdin

amount_vertexes = int(stdin.readline())

adjacency_matrix = [list(map(int, stdin.readline().split())) for _ in range(amount_vertexes)]

adjacency_list = {ind_ver : [i + 1 for i in range(amount_vertexes) if adjacency_matrix[ind_ver - 1][i] == 1] for ind_ver in range(1, amount_vertexes + 1)}

print(adjacency_list)