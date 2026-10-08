working_deque = []

input_strings = ""

while(True):
    input_strings = input().strip().split()

    if(input_strings[0] == "push_front"):
        if(len(working_deque) == 100):
            del working_deque[-1]
        working_deque = [int(input_strings[1])] + working_deque
        print("ok")
    elif(input_strings[0] == "push_back"):
        if(len(working_deque) == 100):
            del working_deque[0]
        working_deque.append(int(input_strings[1]))
        print("ok")
    elif(input_strings[0] == "pop_front"):
        if(len(working_deque) != 0):
            print(working_deque.pop(0))
        else:
            print("error")
    elif(input_strings[0] == "pop_back"):
        if(len(working_deque) != 0):
            print(working_deque.pop())
        else:
            print("error")
    elif(input_strings[0] == "front"):
        if(len(working_deque) != 0):
            print(working_deque[0])
        else:
            print("error")
    elif(input_strings[0] == "back"):
        if(len(working_deque) != 0):
            print(working_deque[-1])
        else:
            print("error")
    elif(input_strings[0] == "size"):
        print(len(working_deque))
    elif(input_strings[0] == "clear"):
        working_deque.clear()
        print("ok")
    elif(input_strings[0] == "exit"):
        print("bye")
        break