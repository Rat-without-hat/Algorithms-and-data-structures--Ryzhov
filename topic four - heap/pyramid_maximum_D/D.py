import heapq
from sys import stdin

max_heap = []

for input_str in stdin:
    input_str = list(input_str.split())

    if(input_str[0] == "CLEAR"):
        max_heap.clear()
    elif(input_str[0] == "ADD"):
        heapq.heappush(max_heap, -int(input_str[1]))
    elif(input_str[0] == "EXTRACT"):
        if(len(max_heap) > 0):
            print(-heapq.heappop(max_heap))
        else:
            print("CANNOT")