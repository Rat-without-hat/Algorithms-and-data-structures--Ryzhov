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
        self._depth = 0

    """
        Метод вставки новых узлов в дерево
    """
    def insert(self, new_val):
        if(self._root is None):
            self._root = Tree.Node(new_val)
            self._depth = 1
        else:
            cur_node = self._root
            pos_depth = 1

            while(True):
                if(cur_node.data > new_val):

                    pos_depth += 1

                    if(cur_node.left is None):
                        cur_node.left = Tree.Node(new_val)
                        break
                    
                    cur_node = cur_node.left
                elif(cur_node.data < new_val):

                    pos_depth += 1

                    if(cur_node.right is None):
                        cur_node.right = Tree.Node(new_val)
                        break
                    
                    cur_node = cur_node.right
                else:
                    break

            if(pos_depth > self._depth):
                self._depth = pos_depth 

    """
        Метода вывода количества уровней в дереве
    """
    def get_level(self):
        return self._depth


work_tree = Tree()

for el in map(int, stdin.readline().split()):
    if(el == 0):
        break
    work_tree.insert(el)

print(work_tree.get_level())