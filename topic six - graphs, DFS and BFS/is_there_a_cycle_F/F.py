from sys import stdin

def dsf(source_graph, status_list, start_ver):
    global res_bool
    status_list[start_ver] = 1

    for close_ver in source_graph[start_ver]:
        if(status_list[close_ver] == 0):
            dsf(source_graph, status_list, close_ver)
        elif(status_list[close_ver] == 1):
            res_bool = 1

    status_list[start_ver] = 2   


amount_vertexes = int(stdin.readline())

adjacency_matrix = [list(map(int, stdin.readline().split())) for _ in range(amount_vertexes)]

adjacency_list = {ind_ver : [i for i in range(amount_vertexes) if adjacency_matrix[ind_ver][i] == 1] 
                  for ind_ver in range(amount_vertexes)}

list_status = [0 for _ in range(amount_vertexes)]

'''
    0 - White (Not touched)
    1 - Grey (Started)
    2 - Black (Completed)
'''

res_bool = 0

for ind_ver in range(amount_vertexes):
    if(list_status[ind_ver] == 0):
        dsf(adjacency_list, list_status, ind_ver)

    if(res_bool):
        break

print(res_bool)