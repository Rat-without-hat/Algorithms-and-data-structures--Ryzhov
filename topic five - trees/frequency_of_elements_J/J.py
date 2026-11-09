class Tree:

    """
        Реализация врутреннего класса Node, узлов дерева
    """
    class Node:
        def __init__(self, data = None):
            self.data = data 
            self.left = None
            self.right = None
            self.amount = 1 if not(data is None) else 0

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
                    cur_node.amount += 1
                    break

    """
        Метод вывода дерева в порядке возрастания
    """
    def print_order_up(self):
        self._print_order_up(self._root)

    def _print_order_up(self, source_node):
        if(source_node is None):
            return
        else:
            self._print_order_up(source_node.left)
            print(source_node.data, source_node.amount)
            self._print_order_up(source_node.right)


work_tree = Tree()

for el in map(int, input().split()):
    if(el == 0):
        break
    work_tree.insert(el)

work_tree.print_order_up()