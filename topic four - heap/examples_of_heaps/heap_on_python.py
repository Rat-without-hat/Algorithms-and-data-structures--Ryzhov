class MaxHeap:
    def __init__(self):
        self._data = [0]
        self._size = 0

    def shift_up(self, ind_el):
        if(2 <= ind_el <= self._size):
            while((ind_el//2 > 0) and (self._data[ind_el] >= self._data[ind_el//2])):
                self._data[ind_el], self._data[ind_el//2] = self._data[ind_el//2], self._data[ind_el]
                ind_el //= 2

    def ind_max_child(self, ind_el):
        if(ind_el * 2 + 1 > self._size):
            return ind_el * 2
        elif(self._data[ind_el * 2] > self._data[ind_el * 2 + 1]):
            return ind_el * 2
        return ind_el * 2 + 1
    
    def shift_down(self, ind_el):
        if(1 <= ind_el <= self._size):
            while(ind_el * 2 <= self._size):
                max_son_ind = self.ind_max_child(ind_el)

                if(self._data[ind_el] <= self._data[max_son_ind]):
                    self._data[ind_el], self._data[max_son_ind] = self._data[max_son_ind], self._data[ind_el]
                    ind_el = max_son_ind
                else:
                    break

    def insert(self, ins_val):
        self._data.append(ins_val)
        self._size += 1
        self.shift_up(self._size)

    def get_max(self):
        if(self._size != 0):
            return self._data[1]
        return None

    def del_max(self):
        self._data[1] = self._data.pop()
        self._size -= 1
        self.shift_down(1)

    def __str__(self):
        return " ".join([str(el) for el in self._data[1:]])