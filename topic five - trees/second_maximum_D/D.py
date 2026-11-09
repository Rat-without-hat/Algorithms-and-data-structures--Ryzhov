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
        Метод нахождение второго максимума в дереве
    """
    def get_second_max(self):
        second_max_val = None

        cur_node = self._root
        prev_node = None

        while(not(cur_node.right is None)):
            prev_node = cur_node
            cur_node = cur_node.right

        cur_node = cur_node.left

        if(not(cur_node is None)):
            while(not(cur_node.right is None)):
                cur_node = cur_node.right

        if((not(prev_node is None)) and (not(cur_node is None))):
            second_max_val = max(prev_node.data, cur_node.data)
        elif((prev_node is None) and (not(cur_node is None))):
            second_max_val = cur_node.data
        elif((not(prev_node is None)) and (cur_node is None)):
            second_max_val = prev_node.data
        else:
            second_max_val = self._root.data

        return second_max_val


work_tree = Tree()

for el in map(int, input().split()):
    if(el == 0):
        break
    work_tree.insert(el)

print(work_tree.get_second_max())