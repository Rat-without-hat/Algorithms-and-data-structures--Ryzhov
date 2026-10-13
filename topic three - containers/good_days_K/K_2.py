from collections import deque

cnt_of_days = int(input())
list_of_emotional_weight_days = deque(map(int, input().split()))

sum_of_weight_period = list_of_emotional_weight_days[0]
coordinates_of_period = [1, 1]
cur_ind_min_on_period = 0

best_happiness_of_period = -1
coordinates_of_best_period = [1, 1]

for cur_ind_day in range(1, cnt_of_days):
    possible_ind_min_on_period = cur_ind_min_on_period if list_of_emotional_weight_days[cur_ind_min_on_period] < \
        list_of_emotional_weight_days[cur_ind_day] else cur_ind_day
    
    if(sum_of_weight_period * list_of_emotional_weight_days[cur_ind_min_on_period] <= \
       (sum_of_weight_period + list_of_emotional_weight_days[cur_ind_day]) * possible_ind_min_on_period):
        
        sum_of_weight_period += list_of_emotional_weight_days[cur_ind_day]
        cur_ind_min_on_period = possible_ind_min_on_period
        coordinates_of_period[1] += 1

    elif((sum_of_weight_period * list_of_emotional_weight_days[cur_ind_min_on_period]) > best_happiness_of_period):
        best_happiness_of_period = sum_of_weight_period * list_of_emotional_weight_days[cur_ind_min_on_period]
        coordinates_of_best_period = coordinates_of_period

        sum_of_weight_period = list_of_emotional_weight_days[cur_ind_day]
        cur_ind_min_on_period = cur_ind_day
        coordinates_of_period = [cur_ind_day, cur_ind_day]

    else:
        sum_of_weight_period = list_of_emotional_weight_days[cur_ind_day]
        cur_ind_min_on_period = cur_ind_day
        coordinates_of_period = [cur_ind_day, cur_ind_day]

    if(coordinates_of_period[1] - coordinates_of_period[0] >= 1):
        possible_ind_max_min_on_period = cur_ind_min_on_period if coordinates_of_period[0] != cur_ind_min_on_period else cur_ind_day

        if(sum_of_weight_period * list_of_emotional_weight_days[cur_ind_min_on_period] < \
           (sum_of_weight_period - list_of_emotional_weight_days[coordinates_of_period[0]]) * possible_ind_max_min_on_period):
            sum_of_weight_period -= list_of_emotional_weight_days[coordinates_of_period[0]]
            cur_ind_min_on_period = possible_ind_max_min_on_period
            coordinates_of_period[0] += 1

print(f"{sum_of_weight_period}\n{coordinates_of_best_period[0]} {coordinates_of_best_period[1]}")
