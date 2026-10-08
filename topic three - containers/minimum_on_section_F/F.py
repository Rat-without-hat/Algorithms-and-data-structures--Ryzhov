len_source_queue, len_sub_queue = list(map(int, input().strip().split()))

sub_queue = []

source_queue = list(map(int, input().strip().split()))

for start_ind in range(0, len_source_queue - len_sub_queue + 1):
    sub_queue = source_queue[start_ind:start_ind + len_sub_queue]

    min_sub_queue = sub_queue[0]
    for ind_sub_deque in range(1, len_sub_queue):
        if(sub_queue[ind_sub_deque] < min_sub_queue):
            min_sub_queue = sub_queue[ind_sub_deque]
    
    print(min_sub_queue)
