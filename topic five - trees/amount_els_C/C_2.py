from sys import stdin

class Tree:

    """
        Реализация врутреннего класса Node, узлов дерева
    """
    class Node:
        def __init__(self, data = None):
            self.data = data 
            self.left = None
            self.right = None

    def __init__(self):
        self._root = None
        self._amount_els = 0

    """
        Метод вставки новых узлов в дерево
    """
    def insert(self, new_val):
        if(self._root is None):
            self._root = Tree.Node(new_val)
            self._amount_els = 1
        else:
            cur_node = self._root

            while(True):
                if(cur_node.data > new_val):
                    if(cur_node.left is None):
                        cur_node.left = Tree.Node(new_val)
                        self._amount_els += 1
                        break
                    
                    cur_node = cur_node.left
                elif(cur_node.data < new_val):
                    if(cur_node.right is None):
                        cur_node.right = Tree.Node(new_val)
                        self._amount_els += 1
                        break
                    
                    cur_node = cur_node.right
                else:
                    break

    """
        Метода вывода количества уровней в дереве
    """
    def get_amount_els(self):
        return self._amount_els


work_tree = Tree()

for el in map(int, stdin.readline().split()):
    if(el == 0):
        break
    work_tree.insert(el)

print(work_tree.get_amount_els())