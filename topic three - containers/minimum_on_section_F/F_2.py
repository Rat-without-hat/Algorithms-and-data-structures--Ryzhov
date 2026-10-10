from collections import deque

def ind_min(source_deque):
    res_min = source_deque[0]
    ind_res_min = 0

    for ind_queue in range(1, len(source_deque)):
        if(source_deque[ind_queue] < res_min):
            res_min = source_deque[ind_queue]
            ind_res_min = ind_queue

    return ind_res_min

len_source_queue, len_sub_deque = list(map(int, input().split()))

source_queue = list(map(int, input().split()))

sub_deque = deque(source_queue[0:len_sub_deque], len_sub_deque)

ind_past_min_in_sub_deque = ind_min(sub_deque)

print(source_queue[ind_past_min_in_sub_deque])

start_ind = 0

for end_ind in range(len_sub_deque, len_source_queue):
    sub_deque.append(source_queue[end_ind])
    start_ind += 1

    if(source_queue[end_ind] <= source_queue[ind_past_min_in_sub_deque]):
        ind_past_min_in_sub_deque = end_ind
    elif(ind_past_min_in_sub_deque < start_ind):
        ind_past_min_in_sub_deque = ind_min(sub_deque) + start_ind

    print(source_queue[ind_past_min_in_sub_deque])