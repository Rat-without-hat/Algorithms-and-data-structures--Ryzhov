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

    """
        Метод вставки новых узлов в дерево
    """
    def insert(self, new_val):
        temp_Node = Tree.Node(new_val)
        bool_exist = False

        if(self._root is None):
            self._root = temp_Node
        else:
            cur_node = self._root
            found = False

            while(not(found)):
                if(cur_node.get_data() > temp_Node.get_data()):
                    if(cur_node.get_left() is None):
                        cur_node.set_left(temp_Node)
                        found = True
                    else:
                        cur_node = cur_node.get_left()
                elif(cur_node.get_data() < temp_Node.get_data()):
                    if(cur_node.get_right() is None):
                        cur_node.set_right(temp_Node)
                        found = True
                    else:
                        cur_node = cur_node.get_right()
                else:
                    found = True
                    bool_exist = True

        return bool_exist

    """
        Метод нахождение максимума в поддереве
    """

    def _get_max(self, source_node):
        cur_node = source_node

        while(not(cur_node.get_right() is None)):
            cur_node = cur_node.get_right()
    
        return cur_node.get_data()

    """
        Метод удаления узла с максимальным значением в поддереве
    """  

    def _del_max(self, source_node):
        cur_node = source_node

        if(cur_node is None):
            return None, False
        
        if(not(cur_node.get_right() is None)):
            new_right, res_bool = self._del_max(cur_node.get_right())
            cur_node.set_right(new_right)
            return cur_node, res_bool
        else:
            if(not(cur_node.get_left() is None)):
                return cur_node.get_left() , True
            else:
                return None, True
    
    """
        Метод поиска по ключу в дереве
    """
    def find(self, find_val):
        found = False

        if(not(self._root is None)):
            cur_node = self._root

            while((not(found)) and (not(cur_node is None))):
                if(find_val < cur_node.get_data()):
                    cur_node = cur_node.get_left()
                elif(find_val > cur_node.get_data()):
                    cur_node = cur_node.get_right()
                else:
                    found = True

        return found

    """
        Метод удаления по ключу в дереве
    """
    def del_key(self, key_val):
        self._root, del_bool = self._del_key(self._root, key_val)

        return del_bool

    def _del_key(self, source_node, key_val):
        cur_node = source_node

        if(cur_node is None):
            return None, False
        
        if(key_val < cur_node.get_data()):
            new_left, res_bool = self._del_key(cur_node.get_left(), key_val)
            cur_node.set_left(new_left)
            return cur_node, res_bool
        elif(key_val > cur_node.get_data()):
            new_right, res_bool = self._del_key(cur_node.get_right(), key_val)
            cur_node.set_right(new_right)
            return cur_node, res_bool
        else:
            if((cur_node.get_left() is None) and (cur_node.get_right() is None)):
                return None, True
            elif((not(cur_node.get_left() is None)) and (cur_node.get_right() is None)):
                return cur_node.get_left(), True
            elif((cur_node.get_left() is None) and (not(cur_node.get_right() is None))):
                return cur_node.get_right() , True
            else:
                temp_max = self._get_max(cur_node.get_left())
                new_left, temp_bool = self._del_max(cur_node.get_left())
                cur_node.set_data(temp_max)
                cur_node.set_left(new_left)
                return cur_node, temp_bool

    """
        Метод вывода дерева
    """
    def print_tree(self):
        if(not(self._root is None)):
            self._print_node(self._root.get_left(), 1)

            print(self._root.get_data())

            self._print_node(self._root.get_right(), 1)

    def _print_node(self, source_node, depth):
        if(not(source_node is None)):
            self._print_node(source_node.get_left(), depth + 1)

            for _ in range(depth):
                print(".", end="")
            print(source_node.get_data())

            self._print_node(source_node.get_right(), depth + 1)


work_tree = Tree()

for line in stdin:
    input_str = line.split()

    if(input_str[0] == "ADD"):
        if(not(work_tree.insert(int(input_str[1])))):
            print("DONE")
        else:
            print("ALREADY")
    elif(input_str[0] == "DELETE"):
        if(work_tree.del_key(int(input_str[1]))):
            print("DONE")
        else:
            print("CANNOT")
    elif(input_str[0] == "SEARCH"):
        if(work_tree.find(int(input_str[1]))):
            print("YES")
        else:
            print("NO")
    elif(input_str[0] == "PRINTTREE"):
        work_tree.print_tree()