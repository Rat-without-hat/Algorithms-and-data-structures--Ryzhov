class Stack:

    def __init__(self):
        self._content = []

    def push(self, el):
        self._content.append(el)
        print("ok")

    def pop(self):
        if len(self._content) > 0:
            print(self._content.pop())
        else:
            print("error")

    def back(self):
        if len(self._content) > 0:
            print(self._content[-1])
        else:
            print("error")

    def size(self):
        print(len(self._content))

    def clear(self):
        self._content = []
        print("ok")


work_stack = Stack()

while(1):
    input_data = input().strip().split()

    if input_data[0] == "size":
        work_stack.size()
    elif input_data[0] == "push":
        work_stack.push(int(input_data[1]))
    elif input_data[0] == "pop":
        work_stack.pop()
    elif input_data[0] == "clear":
        work_stack.clear()
    elif input_data[0] == "back":
        work_stack.back()
    elif input_data[0] == "exit":
        print("bye")
        break