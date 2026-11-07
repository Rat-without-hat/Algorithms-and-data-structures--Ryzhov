from sys import stdin

class Tree:

    """
        Реализация врутреннего класса Node, узлов дерева
    """
    class Node:
        def __init__(self, data = None):
            self._data = data 
            self._left = None
            self._right = None

        def get_data(self):
            return self._data

        def get_left(self):
            return self._left

        def get_right(self):
            return self._right

        def set_data(self, new_val):
            self._data = new_val

        def set_left(self, new_node):
            self._left = new_node

        def set_right(self, new_node):
            self._right = new_node

    def __init__(self):
        self._root = None
        self._amount_els = 0

    """
        Метод вставки новых узлов в дерево
    """
    def insert(self, new_val):

        self._amount_els += 1

        if(self._root is None):
            self._root = Tree.Node(new_val)
        else:
            cur_node = self._root
            insert_bool = False

            while(not(insert_bool)):
                if(cur_node.get_data() > new_val):
                    if(cur_node.get_left() is None):
                        cur_node.set_left(Tree.Node(new_val))
                        insert_bool = True
                    else:
                        cur_node = cur_node.get_left()
                elif(cur_node.get_data() < new_val):
                    if(cur_node.get_right() is None):
                        cur_node.set_right(Tree.Node(new_val))
                        insert_bool = True
                    else:
                        cur_node = cur_node.get_right()
                else:
                    insert_bool = True

    def get_amount_els(self):
        return self._amount_els


work_tree = Tree()

for el in map(int, stdin.readline().split()):
    if(el == 0):
        break
    work_tree.insert(el)

print(work_tree.get_amount_els())