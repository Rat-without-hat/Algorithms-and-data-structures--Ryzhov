class Stack:

    def __init__(self):
        self._content = []

    def push(self, el):
        self._content.append(el)

    def pop(self):
        if len(self._content) > 0:
            del self._content[-1]

    def back(self):
        if len(self._content) > 0:
            return self._content[-1]

    def size(self):
        return len(self._content)

    def clear(self):
        self._content = []

last_ind_wagon_on_second_way = 0

cnt_wagons_on_first_way = int(input())

wagons_on_first_way = list(map(int, input().strip().split()))

stack_wagons_in_berween = Stack()

cur_ind_wagon_on_first_way = 0

while(True):
    if(cur_ind_wagon_on_first_way != cnt_wagons_on_first_way):
        if(wagons_on_first_way[cur_ind_wagon_on_first_way] - last_ind_wagon_on_second_way == 1):
            last_ind_wagon_on_second_way += 1
            cur_ind_wagon_on_first_way += 1
        elif((stack_wagons_in_berween.size() != 0) and (stack_wagons_in_berween.back() - last_ind_wagon_on_second_way == 1)):
            last_ind_wagon_on_second_way += 1
            stack_wagons_in_berween.pop()
        else:
            stack_wagons_in_berween.push(wagons_on_first_way[cur_ind_wagon_on_first_way])
            cur_ind_wagon_on_first_way += 1
    elif((stack_wagons_in_berween.size() != 0) and (stack_wagons_in_berween.back() - last_ind_wagon_on_second_way == 1)):
        last_ind_wagon_on_second_way += 1
        stack_wagons_in_berween.pop()
    else:
        break

if(last_ind_wagon_on_second_way == cnt_wagons_on_first_way):
    print("YES ")
else:
    print("NO")