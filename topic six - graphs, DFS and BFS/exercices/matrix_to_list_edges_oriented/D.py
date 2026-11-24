from sys import stdin

amount_vertexes = int(stdin.readline())

adjacency_matrix = [list(map(int, stdin.readline().split())) for _ in range(amount_vertexes)]

for i in range(amount_vertexes):
    for j in range(amount_vertexes):
        if(adjacency_matrix[i][j] == 1):
            print(f"{i + 1} {j + 1}")