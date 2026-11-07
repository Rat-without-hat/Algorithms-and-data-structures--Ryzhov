class Tree:

    """
        Реализация врутреннего класса Node, узлов дерева
    """
    class Node:
        def __init__(self, data = None):
            self._data = data 
            self._left = None
            self._right = None
            self._level = 1

        def get_data(self):
            return self._data

        def get_left(self):
            return self._left

        def get_right(self):
            return self._right

        def get_level(self):
            return self._level

        def set_data(self, new_val):
            self._data = new_val

        def set_left(self, new_node):
            if(self._level - new_node.get_level() == 0):
                self._level = new_node.get_level() + 1
            self._left = new_node

        def set_right(self, new_node):
            if(self._level - new_node.get_level() == 0):
                self._level = new_node.get_level() + 1
            self._right = new_node

    """
        Метод вставки новых узлов в дерево
    """
    def insert(self, new_val):
        temp_Node = Tree.Node(new_val)

        self._root = self._insert(self._root, temp_Node)

    def _insert(self, source_node, new_node):
        if(source_node is None):
            return new_node

        if(source_node.get_data() > new_node.get_data()):
            if(source_node.get_left() is None):
                source_node.set_left(new_node)
                return source_node
            else:
                source_node.set_left(self._insert(source_node.get_left(), new_node))
                return source_node
        elif(source_node.get_data() < new_node.get_data()):
            if(source_node.get_right() is None):
                source_node.set_right(new_node)
                return source_node
            else:
                source_node.set_right(self._insert(source_node.get_right(), new_node))
                return source_node
        else:
            return source_node

    def __init__(self):
        self._root = None

    """
        Метод нахождение максимума в дереве
    """
    def get_max(self):
        max_val = None

        if(not(self._root is None)):
            max_val = self._get_max(self._root)

        return max_val

    def _get_max(self, source_node):
        cur_node = source_node

        while(not(cur_node.get_right() is None)):
            cur_node = cur_node.get_right()
    
        return cur_node.get_data()

    """
        Метод нахождение минимума в дереве
    """        
    def get_min(self):
        min_val = None

        if(not(self._root is None)):
            min_val = self._get_min(self._root)

        return min_val

    def _get_min(self, source_node):
        cur_node = source_node

        while(not(cur_node.get_left() is None)):
            cur_node = cur_node.get_left()

        return cur_node.get_data()

    """
        Метод удаления максимума в дереве
    """  
    def del_max(self):
        self._root, del_bool = self._del_max(self._root)

        return del_bool

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
        Метод удаления минимума в дереве
    """  
    def del_min(self):
        self._root, del_bool = self._del_min(self._root)

        return del_bool

    def _del_min(self, source_node):
        cur_node = source_node

        if(cur_node is None):
            return None, False
        
        if(not(cur_node.get_left() is None)):
            new_left, res_bool = self._del_min(cur_node.get_left())
            cur_node.set_left(new_left)
            return cur_node, res_bool
        else:
            if(not(cur_node.get_right() is None)):
                return cur_node.get_right() , True
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

    """
        Метода вывода количества уровней в дереве
    """
    def get_level(self):
        return self._root.get_level()