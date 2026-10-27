class MinHeap:
    def __init__(self):
        self._heap = [0]
        self._size = 0

    def shift_up(self, ind_el):
        while((ind_el//2 > 0) and (self._heap[ind_el] < self._heap[ind_el//2])):
            self._heap[ind_el], self._heap[ind_el//2] = self._heap[ind_el//2], self._heap[ind_el]
            ind_el //= 2

    def ind_min_child(self, ind_el):
        if(ind_el * 2 + 1 > self._size):
            return ind_el * 2
        
        if(self._heap[ind_el * 2] < self._heap[ind_el * 2 + 1]):
            return ind_el * 2

        return ind_el * 2 + 1

    def shift_down(self, ind_el):
        while(ind_el * 2 <= self._size):
            ind_child_min = self.ind_min_child(ind_el)

            if(self._heap[ind_el] > self._heap[ind_child_min]):
                self._heap[ind_el], self._heap[ind_child_min] = self._heap[ind_child_min], self._heap[ind_el]
                ind_el = ind_child_min
            else:
                break

    def insert(self, new_el):
        self._heap.append(new_el)
        self._size += 1
        self.shift_up(self._size)

    def extract(self):
        self._heap[1], self._heap[self._size] = self._heap[self._size], self._heap[1]
        max_val = self._heap.pop()
        self._size -= 1
        self.shift_down(1)

        return max_val


amount_els = int(input())
list_els = list(map(int, input().split()))
heap_els = MinHeap()

for _ in range(amount_els):
    heap_els.insert(list_els.pop())

for _ in range(amount_els):
    print(heap_els.extract(), end=" ")