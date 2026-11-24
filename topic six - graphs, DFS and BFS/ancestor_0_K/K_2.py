from sys import stdin 
from collections import deque

amount_vertexes = int(stdin.readline())

adjacency_list = {ind_ver : [] for ind_ver in range(1, amount_vertexes + 1)}

list_parents = list(map(int, stdin.readline().split()))

list_parents = [(ind_ver, list_parents[ind_ver - 1]) for ind_ver in range(1, amount_vertexes + 1)]

list_parents.sort()

for ver, parent_ver in list_parents:
    if(parent_ver != 0):
        adjacency_list[ver].append(parent_ver)
        adjacency_list[ver].extend(adjacency_list[parent_ver])

amount_ops = int(stdin.readline())

for _ in range(amount_ops):
    end_ver, cur_ver = map(int, stdin.readline().split())

    print(int(end_ver in adjacency_list[cur_ver]))