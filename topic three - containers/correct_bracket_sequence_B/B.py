stack_bracket = []

input_bracket = input().strip()

cur_examened_ind = 0

while(cur_examened_ind < len(input_bracket)):

    if(input_bracket[cur_examened_ind] in "({["):
        stack_bracket.append(input_bracket[cur_examened_ind])
    else:
        if(len(stack_bracket) != 0):
            if((stack_bracket[-1] == "(" and input_bracket[cur_examened_ind] == ")") or 
            (stack_bracket[-1] == "{" and input_bracket[cur_examened_ind] == "}") or
            (stack_bracket[-1] == "[" and input_bracket[cur_examened_ind] == "]")):
                stack_bracket.pop()
            else:
                break
        else:
            break

    cur_examened_ind += 1

if((len(stack_bracket) == 0) and (cur_examened_ind == len(input_bracket))):
    print("yes")
else:
    print("no")