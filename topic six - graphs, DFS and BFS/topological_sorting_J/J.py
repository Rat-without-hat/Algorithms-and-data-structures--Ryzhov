from sys import stdin

amount_vertexes, amount_edges = map(int, stdin.readline().split())
adjacency_list = {ind_ver : [] for ind_ver in range(1, amount_vertexes + 1)}

for _ in range(amount_edges):
    vertex_1, vertex_2 = map(int, stdin.readline().split())
    adjacency_list[vertex_1].append(vertex_2)

topological_list = list(map(int, stdin.readline().split()))

list_status = [False for _ in range(amount_vertexes)]
bool_topological = True

for cur_ver in topological_list:
    list_status[cur_ver - 1] = True

    for close_ver in adjacency_list[cur_ver]:
        if(list_status[close_ver - 1]):
            bool_topological = False

    if(not(bool_topological)):
        break

if(bool_topological):
    print("YES")
else:
    print("NO")