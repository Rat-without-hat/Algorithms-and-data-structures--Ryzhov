from collections import deque

line_of_balls = list(map(int, input().split())) + [-1]

possible_del_balls = deque([-1, -2])
res_deleted_balls = 0

cnt_same_balls = 1

for i in range(1, line_of_balls[0] + 2):
    if(line_of_balls[i] != possible_del_balls[-1]):
        if(cnt_same_balls >= 3):
            for _ in range(cnt_same_balls):
                possible_del_balls.pop()
            res_deleted_balls += cnt_same_balls

            if((possible_del_balls[-1] == possible_del_balls[-2]) and (possible_del_balls[-1] == line_of_balls[i])):
                cnt_same_balls = 2
            else:
                cnt_same_balls = 1
        else:
            cnt_same_balls = 1
        
    if(line_of_balls[i] == possible_del_balls[-1]):
        cnt_same_balls += 1

    possible_del_balls.append(line_of_balls[i])
    
print(res_deleted_balls)