class Deque:

    def __init__(self):
        self._content = []

    def push_front(self, el):
        if(len(self._content) == 100):
            del self._content[-1]
        self._content = [el] + self._content
        print("ok")

    def push_back(self, el):
        if(len(self._content) == 100):
            del self._content[0]
        self._content.append(el)
        print("ok")

    def pop_front(self):
        if(len(self._content) != 0):
            print(self._content.pop(0))
        else:
            print("error")

    def pop_back(self):
        if(len(self._content) != 0):
            print(self._content.pop())
        else:
            print("error")

    def front(self):
        if(len(self._content) != 0):
            print(self._content[0])
        else:
            print("error")

    def back(self):
        if(len(self._content) != 0):
            print(self._content[-1])
        else:
            print("error")

    def size(self):
        print(len(self._content))

    def clear(self):
        self._content.clear()
        print("ok")

working_deque = Deque()

input_strings = ""

while(True):
    input_strings = input().strip().split()

    if(input_strings[0] == "push_front"):
        working_deque.push_front(int(input_strings[1]))
    elif(input_strings[0] == "push_back"):
        working_deque.push_back(int(input_strings[1]))
    elif(input_strings[0] == "pop_front"):
        working_deque.pop_front()
    elif(input_strings[0] == "pop_back"):
        working_deque.pop_back()
    elif(input_strings[0] == "front"):
        working_deque.front()
    elif(input_strings[0] == "back"):
        working_deque.back()
    elif(input_strings[0] == "size"):
        working_deque.size()
    elif(input_strings[0] == "clear"):
        working_deque.clear()
    elif(input_strings[0] == "exit"):
        print("bye")
        break