class Queue:

    def __init__(self):
        self._content = []

    def push(self, el):
        self._content.append(int(input_strings[1]))
        print("ok")

    def pop(self):
        if(len(self._content) != 0):
            print(self._content.pop(0))
        else:
            print("error")

    def front(self):
        if(len(self._content) != 0):
            print(self._content[0])
        else:
            print("error")

    def size(self):
        print(len(self._content))

    def clear(self):
        self._content.clear()
        print("ok")

working_queue = Queue()

input_strings = ""

while(True):
    input_strings = input().strip().split()

    if(input_strings[0] == "push"):
        working_queue.push(int(input_strings[1]))
    elif(input_strings[0] == "pop"):
        working_queue.pop()
    elif(input_strings[0] == "front"):
        working_queue.front()
    elif(input_strings[0] == "size"):
        working_queue.size()
    elif(input_strings[0] == "clear"):
        working_queue.clear()
    elif(input_strings[0] == "exit"):
        print("bye")
        break
    