'''
    Реализация алгоритма обхода графа в глубину ниже реализована для списка смежности
'''

def dfs(source_graph, visited_vers, cur_ver):
    visited_vers[cur_ver] = 1

    for close_ver in source_graph[cur_ver]:
        if(visited_vers[close_ver] == 0):
            dfs(source_graph, visited_vers, close_ver)

'''
    Реализация алгоритма обхода графа в глубину ниже реализована для матрицы смежности
'''

def dfs(source_graph, visited_vers, cur_ver):
    global amount_vertexes

    visited_vers[cur_ver] = 1

    for ind_close_ver in range(amount_vertexes):
        if(ind_close_ver != cur_ver):
            if((source_graph[cur_ver][ind_close_ver] == 1) and (visited_vers[ind_close_ver] != 1)):
                dfs(source_graph, visited_vers, ind_close_ver)