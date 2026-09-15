from random import randint


def quick_sort_increase(source_list, left, right):
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
            quick_sort_increase(source_list, left, r)
        if right > l:
            quick_sort_increase(source_list, l, right)


def quick_sort_decrease(source_list, left, right):
    if left < right:
        l = left
        r = right
        val = source_list[randint(left, right)]
        while l <= r:
            while source_list[l] > val:
                l += 1
            while source_list[r] < val:
                r -= 1
            if l <= r:
                source_list[l], source_list[r] = source_list[r], source_list[l]
                l += 1
                r -= 1
        if left < r:
            quick_sort_decrease(source_list, left, r)
        if right > l:
            quick_sort_decrease(source_list, l, right)


list_dist = list(map(int, input().split()))
list_cost = list(map(int, input().split()))

quick_sort_increase(list_dist, 0, len(list_dist) - 1)
quick_sort_decrease(list_cost, 0, len(list_cost) - 1)

res = sum([list_dist[i] * list_cost[i] for i in range(len(list_dist))])

print(res)
