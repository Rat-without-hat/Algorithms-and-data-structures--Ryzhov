from sys import stdin
from collections import deque

size_board = int(stdin.readline())

x_start, y_start = map(int, stdin.readline().split())
x_end, y_end = map(int, stdin.readline().split())

matrix_dist = [[-1 for _ in range(size_board)] for _ in range(size_board)]
matrix_prev = [[None for _ in range(size_board)] for _ in range(size_board)]
next_pos = deque()

matrix_dist[y_start - 1][x_start - 1] = 0
next_pos.append((x_start - 1, y_start - 1))

while(next_pos):
    cur_pos = next_pos.popleft()
    
    if(0 <= cur_pos[0] - 1):
        if(0 <= cur_pos[1] - 2):
            if(matrix_dist[cur_pos[1] - 2][cur_pos[0] - 1] == -1):
                next_pos.append((cur_pos[0] - 1, cur_pos[1] - 2))
                matrix_prev[cur_pos[1] - 2][cur_pos[0] - 1] = cur_pos
                matrix_dist[cur_pos[1] - 2][cur_pos[0] - 1] = matrix_dist[cur_pos[1]][cur_pos[0]] + 1
        if(cur_pos[1] + 2 < size_board):
            if(matrix_dist[cur_pos[1] + 2][cur_pos[0] - 1] == -1):
                next_pos.append((cur_pos[0] - 1, cur_pos[1] + 2))
                matrix_prev[cur_pos[1] + 2][cur_pos[0] - 1] = cur_pos
                matrix_dist[cur_pos[1] + 2][cur_pos[0] - 1] = matrix_dist[cur_pos[1]][cur_pos[0]] + 1

    if(0 <= cur_pos[0] - 2):
        if(0 <= cur_pos[1] - 1):
            if(matrix_dist[cur_pos[1] - 1][cur_pos[0] - 2] == -1):
                next_pos.append((cur_pos[0] - 2, cur_pos[1] - 1))
                matrix_prev[cur_pos[1] - 1][cur_pos[0] - 2] = cur_pos
                matrix_dist[cur_pos[1] - 1][cur_pos[0] - 2] = matrix_dist[cur_pos[1]][cur_pos[0]] + 1
        if(cur_pos[1] + 1 < size_board):
            if(matrix_dist[cur_pos[1] + 1][cur_pos[0] - 2] == -1):
                next_pos.append((cur_pos[0] - 2, cur_pos[1] + 1))
                matrix_prev[cur_pos[1] + 1][cur_pos[0] - 2] = cur_pos
                matrix_dist[cur_pos[1] + 1][cur_pos[0] - 2] = matrix_dist[cur_pos[1]][cur_pos[0]] + 1

    if(cur_pos[0] + 1 < size_board):
        if(0 <= cur_pos[1] - 2):
            if(matrix_dist[cur_pos[1] - 2][cur_pos[0] + 1] == -1):
                next_pos.append((cur_pos[0] + 1, cur_pos[1] - 2))
                matrix_prev[cur_pos[1] - 2][cur_pos[0] + 1] = cur_pos
                matrix_dist[cur_pos[1] - 2][cur_pos[0] + 1] = matrix_dist[cur_pos[1]][cur_pos[0]] + 1
        if(cur_pos[1] + 2 < size_board):
            if(matrix_dist[cur_pos[1] + 2][cur_pos[0] + 1] == -1):
                next_pos.append((cur_pos[0] + 1, cur_pos[1] + 2))
                matrix_prev[cur_pos[1] + 2][cur_pos[0] + 1] = cur_pos
                matrix_dist[cur_pos[1] + 2][cur_pos[0] + 1] = matrix_dist[cur_pos[1]][cur_pos[0]] + 1

    if(cur_pos[0] + 2 < size_board):
        if(0 <= cur_pos[1] - 1):
            if(matrix_dist[cur_pos[1] - 1][cur_pos[0] + 2] == -1):
                next_pos.append((cur_pos[0] + 2, cur_pos[1] - 1))
                matrix_prev[cur_pos[1] - 1][cur_pos[0] + 2] = cur_pos
                matrix_dist[cur_pos[1] - 1][cur_pos[0] + 2] = matrix_dist[cur_pos[1]][cur_pos[0]] + 1
        if(cur_pos[1] + 1 < size_board):
            if(matrix_dist[cur_pos[1] + 1][cur_pos[0] + 2] == -1):
                next_pos.append((cur_pos[0] + 2, cur_pos[1] + 1))
                matrix_prev[cur_pos[1] + 1][cur_pos[0] + 2] = cur_pos
                matrix_dist[cur_pos[1] + 1][cur_pos[0] + 2] = matrix_dist[cur_pos[1]][cur_pos[0]] + 1

print(matrix_dist[y_end - 1][x_end - 1])

if(matrix_dist[y_end - 1][x_end - 1] >= 0):
    res_path = deque()
    res_path.appendleft(f"{x_end} {y_end} \n")

    prev_ver = matrix_prev[y_end - 1][x_end - 1]
    while(not(prev_ver is None)):
        res_path.appendleft(f"{prev_ver[0] + 1} {prev_ver[1] + 1} \n")
        prev_ver = matrix_prev[prev_ver[1]][prev_ver[0]]

    print("".join(res_path))