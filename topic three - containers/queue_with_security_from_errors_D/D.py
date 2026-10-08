working_queue = []

input_strings = ""

while(True):
    input_strings = input().strip().split()

    if(input_strings[0] == "push"):
        working_queue.append(int(input_strings[1]))
        print("ok")
    elif(input_strings[0] == "pop"):
        if(len(working_queue) != 0):
            print(working_queue.pop(0))
        else:
            print("error")
    elif(input_strings[0] == "front"):
        if(len(working_queue) != 0):
            print(working_queue[0])
        else:
            print("error")
    elif(input_strings[0] == "size"):
        print(len(working_queue))
    elif(input_strings[0] == "clear"):
        working_queue.clear()
        print("ok")
    elif(input_strings[0] == "exit"):
        print("bye")
        break
    