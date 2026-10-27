import heapq

    
amount_aqua = int(input())

heap_aqua = []

for ind_aqua in range(1, amount_aqua + 1):
    amount_fish = int(input())
    time_int = 1000 - amount_fish if amount_fish < 1000 else 1
    item = (time_int, ind_aqua, time_int)
    heap_aqua.append(item)

heapq.heapify(heap_aqua)

pos_lab_tech = 1
correct_work = True
time_cor_work = 0

while(correct_work):
    cur_aqua = heapq.heappop(heap_aqua)
    if((time_cor_work + abs(pos_lab_tech - cur_aqua[1])) <= cur_aqua[0]):
        time_cor_work += (cur_aqua[0] - time_cor_work)
        pos_lab_tech = cur_aqua[1]
        new_int = cur_aqua[2] - 1 if cur_aqua[2] > 1 else 1
        heapq.heappush(heap_aqua, (time_cor_work + new_int, cur_aqua[1], new_int))
    else:
        time_cor_work += (cur_aqua[0] - time_cor_work)
        correct_work = False

print(time_cor_work)
