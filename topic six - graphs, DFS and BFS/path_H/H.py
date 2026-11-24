from sys import stdin
from collections import deque

amount_vertexes = int(stdin.readline())

adjacency_list = {ind_ver : [] for ind_ver in range(amount_vertexes)}

for cur_ver in range(amount_vertexes):
    cur_ver_out = list(map(int, stdin.readline().split()))

    for ver in range(amount_vertexes):
        if(cur_ver_out[ver] == 1):
            adjacency_list[cur_ver].append(ver) 

start_ver, end_ver = map(int, stdin.readline().split())

list_dist = [-1 for _ in range(amount_vertexes)]
list_prev = [None for _ in range(amount_vertexes)]
queue_next = deque()

queue_next.append(start_ver - 1)
list_dist[start_ver - 1] = 0

while(queue_next):
    cur_ver = queue_next.popleft()

    for close_ver in adjacency_list[cur_ver]:
        if(list_dist[close_ver] == -1):
            queue_next.append(close_ver)
            list_dist[close_ver] = list_dist[cur_ver] + 1
            list_prev[close_ver] = cur_ver + 1

print(list_dist[end_ver - 1])

if(list_dist[end_ver - 1] > 0):
    res_path = deque()
    res_path.appendleft(end_ver)

    prev_ver = list_prev[end_ver - 1]
    while(not(prev_ver is None)):
        res_path.appendleft(prev_ver)
        prev_ver = list_prev[prev_ver - 1]

    print(" ".join(list(map(str, res_path))))