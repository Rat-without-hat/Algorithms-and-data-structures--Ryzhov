from sys import stdin

amount_vertexes = int(stdin.readline())

adjacency_matrix = [list(map(int, stdin.readline().split())) for _ in range(amount_vertexes)]

bool_oriented = False

for i in range(amount_vertexes):
    if(adjacency_matrix[i][i] == 1):
        bool_oriented = True

    j = 0

    while((not(bool_oriented)) and (j <= (amount_vertexes - i - 1))):
        if(adjacency_matrix[i][i + j] != adjacency_matrix[i + j][i]):
            bool_oriented = True
        j += 1

    if(bool_oriented):
        break

if(bool_oriented):
    print("NO")
else:
    print("YES")
            