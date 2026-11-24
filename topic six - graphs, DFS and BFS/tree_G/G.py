from sys import stdin

def dfs(source_graph, status_list, cur_ver, prev_ver = -1):
    global bool_cycle
    status_list[cur_ver] = True

    for close_ver in source_graph[cur_ver]:
        if(not(status_list[close_ver])):
            dfs(source_graph, status_list, close_ver, prev_ver = cur_ver)
        elif(prev_ver != close_ver):
            bool_cycle = True


amount_vertexes, amount_edges = map(int, stdin.readline().split())

adjacency_list = {ind_ver : []  for ind_ver in range(amount_vertexes)}

for _ in range(amount_edges):
    vertex_1, vertex_2 = map(int, stdin.readline().split())
    adjacency_list[vertex_1 - 1].append(vertex_2 - 1)
    adjacency_list[vertex_2 - 1].append(vertex_1 - 1)

list_status = [False for _ in range(amount_vertexes)]

'''
    0 - White (Not touched)
    1 - Grey (Started)
    2 - Black (Completed)
'''

bool_cycle = False

dfs(adjacency_list, list_status, 0)

if((list_status.count(0) == 0) and (not(bool_cycle))):
    print("YES")
else:
    print("NO")