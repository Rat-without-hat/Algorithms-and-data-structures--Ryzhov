def merge(left_list, right_list):
    res_list = []
    i = 0
    j = 0

    while (i < len(left_list)) and (j < len(right_list)):
        if left_list[i] <= right_list[j]:
            res_list.append(left_list[i])
            i += 1
        else:
            res_list.append(right_list[j])
            j += 1

    res_list += left_list[i:] + right_list[j:]

    return res_list


def merge_sort(source_list):
    if len(source_list) <= 1:
        return source_list

    mid_index = len(source_list) // 2
    left_list = merge_sort(source_list[:mid_index])
    right_list = merge_sort(source_list[mid_index:])

    return merge(left_list, right_list)

len_list = int(input())

source_list = list(map(int, [el for el in input().split() if el != ""]))

source_list = merge_sort(source_list)

for i in range(len_list):
    print(source_list[i], end=" ")