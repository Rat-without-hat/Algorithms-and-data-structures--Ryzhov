import re

stack = []

input_str = input().strip().split()

for cur_examined_ind in range(0, len(input_str)):

    if(re.fullmatch(r"[-+]?\d+(?:\.\d+)?", input_str[cur_examined_ind])):
        stack.append(input_str[cur_examined_ind])
    else:
       stack.append(str(eval(stack.pop(-2) + input_str[cur_examined_ind] + stack.pop())))

    cur_examined_ind += 1

print(stack[0])