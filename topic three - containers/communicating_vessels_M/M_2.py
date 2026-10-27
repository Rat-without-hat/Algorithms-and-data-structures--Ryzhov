from sys import stdin

amount_sections, vol_water = map(int, input().split())

list_height_section = []
list_vol_water_per_section = [0] * amount_sections

list_height_section.append(2 * 10**9 + 1)

for ind, input_height in enumerate(stdin, 0):
    if(ind == (amount_sections - 1)):
        break

    list_height_section.append(int(input_height)) 

list_height_section.append(2 * 10**9 + 1)

ind_first_fill_section = 0
ind_last_fill_section = 0

while(vol_water):
    min_height_to_fill = list_height_section[ind_last_fill_section + 1] \
        if list_height_section[ind_last_fill_section + 1] < list_height_section[ind_last_fill_section] else \
        list_height_section[ind_last_fill_section]

    if((vol_water >= min_height_to_fill) and (list_vol_water_per_section[ind_last_fill_section] < min_height_to_fill)):
        vol_water -= min_height_to_fill
        list_vol_water_per_section[ind_last_fill_section] += min_height_to_fill
        if(list_vol_water_per_section[ind_first_fill_section] != list_vol_water_per_section[ind_last_fill_section]):
            ind_first_fill_section = ind_last_fill_section
    elif(list_vol_water_per_section[ind_last_fill_section] < min_height_to_fill):
        list_vol_water_per_section[ind_last_fill_section] += vol_water
        vol_water = 0

    if(list_vol_water_per_section[ind_last_fill_section] == list_height_section[ind_last_fill_section + 1]):
        ind_last_fill_section += 1
    else:
        min_last_height_to_fill = list_height_section[ind_first_fill_section] \
                if list_height_section[ind_first_fill_section] < list_height_section[ind_last_fill_section + 1] else \
                list_height_section[ind_last_fill_section + 1]
        
        if(vol_water >= (min_last_height_to_fill - list_vol_water_per_section[ind_last_fill_section]) \
           * (ind_last_fill_section - ind_first_fill_section + 1)):
            vol_water -= (min_last_height_to_fill - list_vol_water_per_section[ind_last_fill_section]) \
           * (ind_last_fill_section - ind_first_fill_section + 1)
            for i in range(ind_first_fill_section, ind_last_fill_section + 1):
                list_vol_water_per_section[i] += \
                    min_last_height_to_fill - list_vol_water_per_section[ind_last_fill_section]
        else:
            for i in range(ind_first_fill_section, ind_last_fill_section + 1):
                list_vol_water_per_section[i] += vol_water / (ind_last_fill_section - ind_first_fill_section + 1)
            vol_water = 0

    while((ind_first_fill_section > 0) and \
          (list_vol_water_per_section[ind_first_fill_section] == list_vol_water_per_section[ind_first_fill_section - 1])):
        ind_first_fill_section -= 1

for i in range(amount_sections):
    print(f"{list_vol_water_per_section[i]:.6f}")   