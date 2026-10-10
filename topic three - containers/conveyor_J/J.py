from collections import deque
from sys import stdin

cnt_tests = int(stdin.readline())

storage_for_containers = deque()

for ind_test, input_test in enumerate(stdin, 1):
    cur_test = deque(list(map(float, input_test.split())))
    cnt_containers = int(cur_test.popleft())
    cur_test_sorted = sorted(cur_test, reverse = True)

    possible_cnt_sort_for_test = 0
    while(True):
        if((storage_for_containers) and (storage_for_containers[-1] == cur_test_sorted[-1])):
            cur_test_sorted.pop()
            storage_for_containers.pop()
            possible_cnt_sort_for_test += 1
        elif((cur_test) and (cur_test[0] == cur_test_sorted[-1])):
            cur_test_sorted.pop()
            cur_test.popleft()
            possible_cnt_sort_for_test += 1
        elif(cur_test):
            storage_for_containers.append(cur_test.popleft())
        else:
            break

    storage_for_containers.clear()

    if(cnt_containers == possible_cnt_sort_for_test):
        print(1)
    else:
        print(0)
    
    if(ind_test == cnt_tests):
        break


