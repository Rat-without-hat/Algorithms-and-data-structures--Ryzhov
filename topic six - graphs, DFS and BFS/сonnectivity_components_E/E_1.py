from sys import stdin, setrecursionlimit

setrecursionlimit(100000)

def dfs(source_graph, visited_vers, cur_group, cur_ver):
    visited_vers[cur_ver - 1] = True
    cur_group.append(cur_ver)

    for close_ver in source_graph[cur_ver]:
        if(visited_vers[close_ver - 1] == False):
            dfs(source_graph, visited_vers, cur_group, close_ver)


amount_vertexes, amount_edges = map(int, stdin.readline().split())

adjacency_list = {ind_ver : [] for ind_ver in range(1, amount_vertexes + 1)}

for _ in range(amount_edges):
    vertex_1, vertex_2 = map(int, stdin.readline().split())
    adjacency_list[vertex_1].append(vertex_2)
    adjacency_list[vertex_2].append(vertex_1)

list_visited = [False for _ in range(amount_vertexes)]
list_groups = list()

for ind_ver in range(1, amount_vertexes + 1):
    if(not(list_visited[ind_ver - 1])):
        list_groups.append([])
        dfs(adjacency_list, list_visited, list_groups[-1], ind_ver)

print(len(list_groups))
for group in list_groups:
    print(len(group))
    print(" ".join(map(str, group)))