from sys import stdin

amount_vertexes, amount_edges = map(int, stdin.readline().split())

adjacency_list = {ind_ver : [] for ind_ver in range(amount_vertexes)}

for _ in range(amount_edges):
    vertex_1, vertex_2 = map(int, stdin.readline().split())
    adjacency_list[vertex_1 - 1].append(vertex_2 - 1)
    adjacency_list[vertex_2 - 1].append(vertex_1 - 1)

list_visited = [False for _ in range(amount_vertexes)]
list_groups = list()

for ind_ver in range(amount_vertexes):
    if(not(list_visited[ind_ver])):

        list_groups.append([])
        stack = [ind_ver]

        while(stack):
            cur_ver = stack.pop()
            if(list_visited[cur_ver]):
                continue

            list_visited[cur_ver] = True
            list_groups[-1].append(cur_ver + 1)

            for neighbor in adjacency_list[cur_ver]:
                if(not(list_visited[neighbor])):
                    stack.append(neighbor)

print(len(list_groups))
for group in list_groups:
    print(len(group))
    print(" ".join(map(str, group)))