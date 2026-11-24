from sys import stdin

def dfs(source_graph, visited_vers, cur_ver):
    visited_vers[cur_ver] = 1

    for close_ver in source_graph[cur_ver]:
        if(visited_vers[close_ver] == 0):
            dfs(source_graph, visited_vers, close_ver)


amount_vertexes, start_vertex = map(int, stdin.readline().split())

adjacency_matrix = [list(map(int, stdin.readline().split())) for _ in range(amount_vertexes)]

adjacency_list = {ind_ver : [i for i in range(amount_vertexes) if adjacency_matrix[ind_ver][i] == 1]
                  for ind_ver in range(amount_vertexes)}

amount_reachable = [0 for _ in range(amount_vertexes)]

dfs(adjacency_list, amount_reachable, start_vertex - 1)

print(sum(amount_reachable))