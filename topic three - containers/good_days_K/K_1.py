from collections import deque

cnt_of_days = int(input())
list_of_emotional_weight_days = list(map(int, input().split()))

max_happiness_of_period = -1
coordinates_of_period = [0, 0]

for ind_min in range(cnt_of_days):
    sum_cur_period = -list_of_emotional_weight_days[ind_min]
    left_day = ind_min
    right_day = ind_min

    while((left_day >= 0) and (list_of_emotional_weight_days[left_day] >= list_of_emotional_weight_days[ind_min])):
        sum_cur_period += list_of_emotional_weight_days[left_day]
        left_day -= 1

    while((right_day <= (cnt_of_days - 1)) and (list_of_emotional_weight_days[right_day] >= list_of_emotional_weight_days[ind_min])):
        sum_cur_period += list_of_emotional_weight_days[right_day]  
        right_day += 1

    if(max_happiness_of_period < (sum_cur_period * list_of_emotional_weight_days[ind_min])):
        max_happiness_of_period = sum_cur_period * list_of_emotional_weight_days[ind_min]
        coordinates_of_period[0] = left_day + 2
        coordinates_of_period[1] = right_day

print(f"{max_happiness_of_period}\n{coordinates_of_period[0]} {coordinates_of_period[1]}")
    
