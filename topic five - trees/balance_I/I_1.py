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
            self.level = 0

    def __init__(self):
        self._root = None

    def _get_level_node(self, source_node):
        return source_node.level if not(source_node is None) else -1
    
    """
        Метод вставки новых узлов в дерево
    """
    def insert(self, new_val):
        self._root = self._insert(self._root, Tree.Node(new_val))

    def _insert(self, source_node, new_node):
        if(source_node is None):
            return new_node

        if(source_node.data > new_node.data):
            if(source_node.left is None):
                source_node.left = new_node
                source_node.level = max(self._get_level_node(source_node.left), self._get_level_node(source_node.right)) + 1
                return source_node
            else:
                source_node.left = self._insert(source_node.left, new_node)
                source_node.level = max(self._get_level_node(source_node.left), self._get_level_node(source_node.right)) + 1
                return source_node
        elif(source_node.data < new_node.data):
            if(source_node.right is None):
                source_node.right = new_node
                source_node.level = max(self._get_level_node(source_node.left), self._get_level_node(source_node.right)) + 1
                return source_node
            else:
                source_node.right = self._insert(source_node.right, new_node)
                source_node.level = max(self._get_level_node(source_node.left), self._get_level_node(source_node.right)) + 1
                return source_node
        else:
            return source_node

    """
        Метод проверки дерева на баланс
    """
    def is_it_balanced(self):
        return self._is_it_balanced(self._root)

    def _is_it_balanced(self, source_node):
        if(source_node is None):
            return True
        else:
            return (abs(self._get_level_node(source_node.left) - self._get_level_node(source_node.right)) <= 1) and \
                        self._is_it_balanced(source_node.left) and self._is_it_balanced(source_node.right)


work_tree = Tree()

for el in map(int, stdin.readline().split()):
    if(el == 0):
        break
    work_tree.insert(el)

if(work_tree.is_it_balanced()):
    print("YES")
else:
    print("NO")