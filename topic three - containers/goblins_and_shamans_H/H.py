from collections import deque
from sys import stdin

list_first_half_goblins = deque()
list_second_half_goblins = deque()

cnt_program_requests = int(stdin.readline())

for _ in range(cnt_program_requests):

    input_line = stdin.readline()
    
    if input_line[0] == "+":
        list_second_half_goblins.append(int(input_line[2:-1]))
    elif input_line[0] == "*":
        list_second_half_goblins.appendleft(int(input_line[2:-1]))
    elif input_line[0] == "-":
        print(list_first_half_goblins.popleft())

    if(len(list_first_half_goblins) < len(list_second_half_goblins)):
        list_first_half_goblins.append(list_second_half_goblins.popleft())