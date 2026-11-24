from sys import stdin 
from collections import deque

amount_vertexes = int(stdin.readline())

oriented_adjacency_list = {ind_ver : -1 for ind_ver in range(1, amount_vertexes + 1)}

list_level = {ind_ver : -1 for ind_ver in range(1, amount_vertexes + 1)}
adjacency_list = {ind_ver : [] for ind_ver in range(1, amount_vertexes + 1)}

list_parents = list(map(int, stdin.readline().split()))

for ver in range(1, len(list_parents) + 1):
    if(list_parents[ver - 1] != 0):
        adjacency_list[ver].append(list_parents[ver - 1])
        oriented_adjacency_list[ver] = list_parents[ver - 1]

        adjacency_list[list_parents[ver - 1]].append(ver)
    else:
        start_ver = ver

queue_next = deque()

queue_next.append(start_ver)
list_level[start_ver] = 0

while(queue_next):
    cur_ver = queue_next.popleft()

    for close_ver in adjacency_list[cur_ver]:
        if(list_level[close_ver] == -1):
            queue_next.append(close_ver)
            list_level[close_ver] = list_level[cur_ver] + 1

amount_ops = int(stdin.readline())

for _ in range(amount_ops):
    end_ver, cur_ver = map(int, stdin.readline().split())

    while(list_level[cur_ver] > list_level[end_ver]):
        cur_ver = oriented_adjacency_list[cur_ver]

    print(int(cur_ver == end_ver))