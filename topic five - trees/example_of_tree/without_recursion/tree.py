from collections import deque

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

        if(self._root is None):
            self._root = temp_Node
        else:
            cur_node = self._root
            insert_bool = False

            while(not(insert_bool)):
                if(cur_node.get_data() > temp_Node.get_data()):
                    if(cur_node.get_left() is None):
                        cur_node.set_left(temp_Node)
                        insert_bool = True
                    else:
                        cur_node = cur_node.get_left()
                elif(cur_node.get_data() < temp_Node.get_data()):
                    if(cur_node.get_right() is None):
                        cur_node.set_right(temp_Node)
                        insert_bool = True
                    else:
                        cur_node = cur_node.get_right()
                else:
                    insert_bool = True

    """
        Метод нахождение максимума в дереве
    """
    def get_max(self):
        max_val = None

        if(not(self._root is None)):
            cur_node = self._root

            while(not(cur_node.get_right() is None)):
                cur_node = cur_node.get_right()

            max_val = cur_node.get_data()
        
        return max_val

    """
        Метод нахождение минимума в дереве
    """        
    def get_min(self):
        min_val = None

        if(not(self._root is None)):
            cur_node = self._root

            while(not(cur_node.get_left() is None)):
                cur_node = cur_node.get_left()

            min_val = cur_node.get_data()

        return min_val

    """
        Метод удаления максимума в дереве
    """  
    def del_max(self):
        if(self._root is None):
            return False

        prev_node = None
        cur_node = self._root
        del_bool = False

        while(not(del_bool)):
            if(not(cur_node.get_right() is None)):
                prev_node = cur_node
                cur_node = cur_node.get_right()
            else:
                if(not(cur_node.get_left() is None)):
                    if(not(prev_node is None)):
                        prev_node.set_right(cur_node.get_left())
                        del_bool = True
                    else:
                        self._root = None
                        del_bool = True
                else:
                    if(not(prev_node is None)):
                        prev_node.set_right(None)
                        del_bool = True
                    else:
                        self._root = None
                        del_bool = True

    """
        Метод удаления минимума в дереве
    """  
    def del_min(self):
        if(self._root is None):
            return False

        prev_node = None
        cur_node = self._root
        del_bool = False

        while(not(del_bool)):
            if(not(cur_node.get_left() is None)):
                prev_node = cur_node
                cur_node = cur_node.get_left()
            else:
                if(not(cur_node.get_right() is None)):
                    if(not(prev_node is None)):
                        prev_node.set_left(cur_node.get_right())
                        del_bool = True
                    else:
                        self._root = None
                        del_bool = True
                else:
                    if(not(prev_node is None)):
                        prev_node.set_left(None)
                        del_bool = True
                    else:
                        self._root = None
                        del_bool = True
    
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
        prev_node = None
        cur_node = self._root

        while(not(cur_node is None)):
            if(cur_node.get_data() > key_val):
               prev_node =  cur_node
               cur_node = cur_node.get_left()
            elif(cur_node.get_data() < key_val):
                prev_node =  cur_node
                cur_node = cur_node.get_right()
            else:
                if(not(prev_node is None)):
                    if((cur_node.get_left() is None) and (cur_node.get_right() is None)):
                        if(prev_node.get_data() < key_val):
                            prev_node.set_right(None)
                            return True
                        else:
                            prev_node.set_left(None)
                            return True
                    elif((not(cur_node.get_left() is None)) and (cur_node.get_right() is None)):
                        if(prev_node.get_data() < key_val):
                            prev_node.set_right(cur_node.get_left())
                            return True
                        else:
                            prev_node.set_left(cur_node.get_left())
                            return True
                    elif((cur_node.get_left() is None) and (not(cur_node.get_right() is None))):
                        if(prev_node.get_data() < key_val):
                            prev_node.set_right(cur_node.get_right())
                            return True
                        else:
                            prev_node.set_left(cur_node.get_right())
                            return True
                    else:
                        prev_node = cur_node
                        second_prev_node = None
                        cur_node = cur_node.get_left()

                        while(not(cur_node.get_right() is None)):
                            second_prev_node = cur_node
                            cur_node = cur_node.get_right()

                        prev_node.set_data(cur_node.get_data())
                        if(second_prev_node == None):
                            prev_node.set_left(None)
                        else:
                            if(not(cur_node.get_left())):
                                second_prev_node.set_right(cur_node.get_left())
                            else:
                                second_prev_node.set_right(None)
                else:
                    if((cur_node.get_left() is None) and (cur_node.get_right() is None)):
                        self._root = None
                        return True
                    elif((not(cur_node.get_left() is None)) and (cur_node.get_right() is None)):
                        self._root = self._root.get_left()
                        return True
                    elif((cur_node.get_left() is None) and (not(cur_node.get_right() is None))):
                        self._root = self._root.get_right()
                        return True
                    else:
                        second_prev_node = None
                        cur_node = self._root.get_left()

                        while(not(cur_node.get_right() is None)):
                            second_prev_node = cur_node
                            cur_node = cur_node.get_right()

                        self._root.set_data(cur_node.get_data())
                        if(second_prev_node == None):
                            self._root.set_left(None)
                        else:
                            if(not(cur_node.get_left())):
                                second_prev_node.set_right(cur_node.get_left())
                            else:
                                second_prev_node.set_right(None)

        return False

    """
        Метод вывода дерева черезх красивое дерево
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

    # Методы ниже без рекурсии сделать проблематично, поэтому их реализацию оставим через нее

    """
        Метод вывода дерева в порядке возрастания
    """
    def order_up(self):

        res_list = []
        cur_node = self._root

        res_list.extend(self._order_up(cur_node.get_left()))
        res_list.append(cur_node.get_data())
        res_list.extend(self._order_up(cur_node.get_right()))

        return res_list

    def _order_up(self, source_node):
        res_list = []

        if((source_node.get_left() is None) and (source_node.get_right() is None)):
            res_list.append(source_node.get_data())
        elif((source_node.get_left() is None) and (not(source_node.get_right() is None))):
            res_list.append(source_node.get_data())
            res_list.extend(self._order_up(source_node.get_right()))
        elif((not(source_node.get_left() is None)) and (source_node.get_right() is None)):
            res_list.extend(self._order_up(source_node.get_left()))
            res_list.append(source_node.get_data())
        else:
            res_list.extend(self._order_up(source_node.get_left()))
            res_list.append(source_node.get_data())
            res_list.extend(self._order_up(source_node.get_right()))

        return res_list

    """
        Метод вывода дерева в порядке убывания
    """
    def order_down(self):

        res_list = []

        res_list.extend(self._order_down(self._root.get_right()))
        res_list.append(self._root.get_data())
        res_list.extend(self._order_down(self._root.get_left()))

        return res_list

    def _order_down(self, source_node):
        res_list = []

        if((source_node.get_left() is None) and (source_node.get_right() is None)):
            res_list.append(source_node.get_data())
        elif((source_node.get_left() is None) and (not(source_node.get_right() is None))):
            res_list.extend(self._order_down(source_node.get_right()))
            res_list.append(source_node.get_data())
        elif((not(source_node.get_left() is None)) and (source_node.get_right() is None)):
            res_list.append(source_node.get_data())
            res_list.extend(self._order_down(source_node.get_left()))
        else:
            res_list.extend(self._order_down(source_node.get_right()))
            res_list.append(source_node.get_data())
            res_list.extend(self._order_down(source_node.get_left()))

        return res_list

    """
        Метод вывода дерева в префиксной форме
    """
    def prefix_order(self):

        res_list = []

        res_list.append(self._root.get_data())
        res_list.extend(self._prefix_order(self._root.get_left()))
        res_list.extend(self._prefix_order(self._root.get_right()))

        return res_list

    def _prefix_order(self, source_node):
        res_list = []

        if((source_node.get_left() is None) and (source_node.get_right() is None)):
            res_list.append(source_node.get_data())
        elif((source_node.get_left() is None) and (not(source_node.get_right() is None))):
            res_list.append(source_node.get_data())
            res_list.extend(self._prefix_order(source_node.get_right()))
        elif((not(source_node.get_left() is None)) and (source_node.get_right() is None)):
            res_list.append(source_node.get_data())
            res_list.extend(self._prefix_order(source_node.get_left()))
        else:
            res_list.append(source_node.get_data())
            res_list.extend(self._prefix_order(source_node.get_left()))
            res_list.extend(self._prefix_order(source_node.get_right()))

        return res_list

    """
        Метод вывода дерева в постфиксной форме
    """
    def postfix_order(self):

        res_list = []


        res_list.extend(self._postfix_order(self._root.get_left()))
        res_list.extend(self._postfix_order(self._root.get_right()))
        res_list.append(self._root.get_data())

        return res_list

    def _postfix_order(self, source_node):
        res_list = []

        if((source_node.get_left() is None) and (source_node.get_right() is None)):
            res_list.append(source_node.get_data())
        elif((source_node.get_left() is None) and (not(source_node.get_right() is None))):
            res_list.extend(self._postfix_order(source_node.get_right()))
            res_list.append(source_node.get_data())
        elif((not(source_node.get_left() is None)) and (source_node.get_right() is None)):
            res_list.extend(self._postfix_order(source_node.get_left()))
            res_list.append(source_node.get_data())
        else:
            res_list.extend(self._postfix_order(source_node.get_left()))
            res_list.extend(self._postfix_order(source_node.get_right()))
            res_list.append(source_node.get_data())

        return res_list

    """
        Метода обхода дерева в ширину
    """
    def breadth_first_search(self):
        vertexes = deque()
        res_list = []

        vertexes.append(self._root)

        while(len(vertexes) != 0):

            cur_vertex = vertexes.popleft()

            if(not(cur_vertex.get_left() is None)):
                vertexes.append(cur_vertex.get_left())
            if(not(cur_vertex.get_right() is None)):
                vertexes.append(cur_vertex.get_right())

            res_list.append(cur_vertex.get_data())

        return res_list


tree = Tree()

tree.insert(8)
tree.insert(10)
tree.insert(3)
tree.insert(6)
tree.insert(1)
tree.insert(7)
tree.insert(14)
tree.insert(4)
tree.insert(13)

tree.print_tree()

print(tree.order_down())
print(tree.order_up())
print(tree.prefix_order())
print(tree.postfix_order())
print(tree.breadth_first_search())