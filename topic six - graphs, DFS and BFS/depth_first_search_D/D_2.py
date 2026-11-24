from sys import stdin


def dfs(source_graph, visited_vers, cur_ver):
    global amount_vertexes

    visited_vers[cur_ver] = 1

    for ind_close_ver in range(amount_vertexes):
        if(ind_close_ver != cur_ver):
            if((source_graph[cur_ver][ind_close_ver] == 1) and (visited_vers[ind_close_ver] != 1)):
                dfs(source_graph, visited_vers, ind_close_ver)


amount_vertexes, start_vertex = map(int, stdin.readline().split())

adjacency_matrix = [list(map(int, stdin.readline().split())) for _ in range(amount_vertexes)]

amount_reachable = [0 for _ in range(amount_vertexes)]

dfs(adjacency_matrix, amount_reachable, start_vertex - 1)

print(sum(amount_reachable))