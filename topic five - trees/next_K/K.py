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
        Метод нахождение минимального элемента, не меньшего val в дереве
    """        
    def get_min_before(self, val):
        cur_node = self._root
        min_val = -1

        while(not(cur_node is None)):
            if(cur_node.data >= val):
                min_val = cur_node.data
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right

        return min_val


work_s = Tree()

cnt_com = int(stdin.readline())
bool_next = False
prev_res = 0
answers = []

for ind_com, str_input in enumerate(stdin, 1):
    cur_com = str_input.split()

    if(cur_com[0] == "+"):
        if(not(bool_next)):
            work_s.insert(int(cur_com[1]))
        else:
            work_s.insert((int(cur_com[1]) + prev_res) % 10**9)
            bool_next = False
    elif(cur_com[0] == "?"):
        bool_next = True
        prev_res = work_s.get_min_before(int(cur_com[1]))
        answers.append(str(prev_res))

    if(ind_com == cnt_com):
        break

print("\n".join(answers))
    