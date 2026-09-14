from random import randint

def quick_sort(source_list, left, right):
    if left < right:
        l = left
        r = right
        val = source_list[randint(left, right)]
        while l <= r:
            while source_list[l] < val:
                l += 1
            while source_list[r] > val:
                r -= 1
            if l <= r:
                source_list[l], source_list[r] = source_list[r], source_list[l]
                l += 1
                r -= 1
        if left < r:
            quick_sort(source_list, left, r)
        if right > l:
            quick_sort(source_list, l, right)


len_list = int(input())

source_string = input()
if source_string != "":
    source_list = list(map(int, [el for el in source_string.split(" ") if el != ""]))
else:
    source_list = []

quick_sort(source_list, 0, len_list - 1)

for i in range(len_list):
    print(source_list[i], end=" ")