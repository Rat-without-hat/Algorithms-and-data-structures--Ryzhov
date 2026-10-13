from sys import stdin

def define_cnt_filled_sections(list_height, volume_water, cur_ind, cnt_filled_sections):
    if(list_height[cur_ind] < volume_water):
        return define_cnt_filled_sections(list_height, volume_water, cur_ind - 1, cnt_filled_sections + 1)
    else:
        return cnt_filled_sections

amount_sections, vol_water = map(int, input().split())

list_height_section = []
list_vol_water_per_section = [0] * amount_sections

list_height_section.append(2 * 10**9 + 1)

for ind, input_height in enumerate(stdin, 0):
    if(ind == (amount_sections - 1)):
        break

    list_height_section.append(int(input_height))

list_height_section.append(2 * 10**9 + 1)
    
ind_last_filled_section = 1

for _ in range(vol_water):

    if(list_vol_water_per_section[ind_last_filled_section] == list_height_section[ind_last_filled_section]):
        ind_last_filled_section += 1
    
    if((list_vol_water_per_section[ind_last_filled_section] < list_height_section[ind_last_filled_section - 1])):
        list_vol_water_per_section[ind_last_filled_section] += 1
    else:
        for filled_sections in range(ind_last_filled_section, 
                                     ind_last_filled_section - define_cnt_filled_sections(list_height_section, vol_water, ind_last_filled_section, 1), 
                                     -1):
            list_vol_water_per_section[filled_sections] += 1 / define_cnt_filled_sections(list_height_section, 
                                                                                          list_vol_water_per_section[ind_last_filled_section], 
                                                                                          ind_last_filled_section, 1)
        


