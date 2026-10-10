from collections import deque

len_source_queue, len_sub_deque = list(map(int, input().split()))

source_queue = list(map(int, input().split()))

min_deque = deque()

for i in range(len_source_queue):
    while min_deque and source_queue[min_deque[-1]] >= source_queue[i]:
        min_deque.pop()

    min_deque.append(i)

    if min_deque[0] <= i - len_sub_deque:
        min_deque.popleft()

    if i >= len_sub_deque - 1:
        print(source_queue[min_deque[0]])