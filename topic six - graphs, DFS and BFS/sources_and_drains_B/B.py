from sys import stdin

list_in = list()
list_out = list()

amount_vertexes = int(stdin.readline())

adjacency_matrix = [list(map(int, stdin.readline().split())) for _ in range(amount_vertexes)]

for ind_vertex in range(amount_vertexes):
    cnt_in_cur_vertex = 0
    cnt_out_cur_vertex = 0

    for j in range(amount_vertexes):
        if(adjacency_matrix[ind_vertex][j] == 1):
            cnt_out_cur_vertex += 1
        if(adjacency_matrix[j][ind_vertex] == 1):
            cnt_in_cur_vertex += 1

    if(cnt_out_cur_vertex == 0):
        list_in.append(ind_vertex + 1)
    if(cnt_in_cur_vertex == 0):
        list_out.append(ind_vertex + 1)

print(len(list_out))
for vertex in list_out:
    print(vertex)

print(len(list_in))
for vertex in list_in:
    print(vertex)