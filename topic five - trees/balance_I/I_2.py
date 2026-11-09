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
        else:
            cur_node = self._root
  
            while(True):
                if(cur_node.data > new_val):
                    if(cur_node.left is None):
                        cur_node.left = Tree.Node(new_val)
                        break
                    cur_node = cur_node.left
                elif(cur_node.data < new_val):
                    if(cur_node.right is None):
                        cur_node.right = Tree.Node(new_val)
                        break 
                    cur_node = cur_node.right
                else:
                    break

    """
        Метод проверки дерева на баланс
    """
    def is_it_balanced(self):
        res_bool, res_level = self._is_it_balanced(self._root)

        return res_bool

    def _is_it_balanced(self, source_node):
        if(source_node is None):
            return True, -1
        
        right_balanced_bool, right_level = self._is_it_balanced(source_node.right)
        left_balanced_bool, left_level = self._is_it_balanced(source_node.left)

        return right_balanced_bool and left_balanced_bool and (abs(right_level - left_level) <= 1), max(right_level, left_level) + 1


work_tree = Tree()

for el in map(int, stdin.readline().split()):
    if(el == 0):
        break
    work_tree.insert(el)

if(work_tree.is_it_balanced()):
    print("YES")
else:
    print("NO")