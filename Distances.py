n, m, k = list(map(int, input().split()))
graph = {}
graph_input = {}

max_int = 999999999999


def delet(input_graph, ver):
    if ver in input_graph:
        output_edges = input_graph[ver]
        del input_graph[ver]
    else:
        output_edges = []
    input_edges = []
    for vertex in input_graph:
        for j in range(len(input_graph[vertex])):
            if input_graph[vertex][j][0] == ver:
                input_edges.append([vertex, input_graph[vertex][j][1]])
                del input_graph[vertex][j]
                break

    return output_edges, input_edges


for i in range(m):
    v1, v2, w = list(map(int, input().split()))
    if v1 - 1 in graph:
        graph[int(v1) - 1].append([int(v2) - 1, w])
    else:
        graph[int(v1) - 1] = [[int(v2) - 1, w]]
    if v2 - 1 in graph_input:
        graph_input[v2 - 1].append([v1 - 1, w])
    else:
        graph_input[v2 - 1] = [[v1 - 1, w]]

answers = []

deleted_node_order = []
queries = []

deleted_node_output = {}
deleted_node_ordering = []

remain_nodes = [i for i in range(n)]
for i in range(k):
    query = list(map(int, input().split()))
    type_of_input = query[0]

    if query[0] == 1:
        v = query[1]
        result = delet(graph, v - 1)
        deleted_node_output[v - 1] = ([result[0], result[1]])
        deleted_node_ordering.append(v - 1)

        deleted_node_order.append(int(v) - 1)
        queries.append([1, int(v) - 1])
        remain_nodes[int(v) - 1] = -1

    if query[0] == 2:
        v1 = query[1]
        v2 = query[2]
        queries.append([2, v1 - 1, v2 - 1])
        # answers.append(distance_matrix[v1, v2])

distance_matrix = [[max_int for _ in range(n)] for _ in range(n)]

other_node = []
for node in remain_nodes:
    if node != -1:
        other_node.append(node)

new_graph_node = []
for node in other_node:
    result = delet(graph, node)
    deleted_node_output[node] = [result[0], result[1]]
    deleted_node_ordering.append(node)

other_node.reverse()


def add_node(this_node_func, added_edges_func, distance_matrix_func, added_func):
    out_dic = {}
    in_dic = {}
    for clause in added_edges_func[0]:
        out_dic[clause[0]] = clause[1]
    for clause in added_edges_func[1]:
        in_dic[clause[0]] = clause[1]

    for i in added_func:
        for j in added_func:
            if i == j:
                distance_matrix_func[i][j] = 0
            else:
                # for k in added:
                alter_i = max_int
                if i in in_dic:
                    alter_i = in_dic[i]
                alter_j = max_int
                if j in out_dic:
                    alter_j = out_dic[j]

                if alter_i > distance_matrix_func[i][this_node_func]:
                    alter_i = distance_matrix_func[i][this_node_func]
                if alter_j > distance_matrix_func[this_node_func][j]:
                    alter_j = distance_matrix_func[this_node_func][j]

                amount_func = alter_i + alter_j
                distance_matrix_func[i][j] = min(distance_matrix_func[i][j], amount_func)

    return distance_matrix_func


added = []

for order in range(len(other_node)):
    this_node = other_node[order]
    added.append(this_node)
    added_edges = deleted_node_output[this_node]

    for l in range(len(added_edges[0])):
        distance_matrix[this_node][added_edges[0][l][0]] = min(distance_matrix[this_node][added_edges[0][l][0]],
                                                               added_edges[0][l][1])
        for i in range(n):
            if i != this_node:
                amount = distance_matrix[added_edges[0][l][0]][i] + distance_matrix[this_node][added_edges[0][l][0]]
                distance_matrix[this_node][i] = min(distance_matrix[this_node][i], amount)

    for l in range(len(added_edges[1])):
        distance_matrix[added_edges[1][l][0]][this_node] = min(distance_matrix[added_edges[1][l][0]][this_node],
                                                               added_edges[1][l][1])
        for i in range(n):
            if i != this_node:
                amount = distance_matrix[i][added_edges[1][l][0]] + distance_matrix[added_edges[1][l][0]][this_node]
                distance_matrix[i][this_node] = min(distance_matrix[i][this_node], amount)

    added_edges = deleted_node_output[this_node]
    distance_matrix = add_node(this_node, added_edges, distance_matrix, added)

queries.reverse()
for query in queries:
    if query[0] == 1:
        this_node = query[1]
        added.append(this_node)
        added_edges = deleted_node_output[this_node]

        for l in range(len(added_edges[0])):
            distance_matrix[this_node][added_edges[0][l][0]] = min(distance_matrix[this_node][added_edges[0][l][0]],
                                                                   added_edges[0][l][1])
            for i in range(n):
                if i != this_node:
                    amount = distance_matrix[added_edges[0][l][0]][i] + distance_matrix[this_node][added_edges[0][l][0]]
                    distance_matrix[this_node][i] = min(distance_matrix[this_node][i], amount)

        for l in range(len(added_edges[1])):
            distance_matrix[added_edges[1][l][0]][this_node] = min(distance_matrix[added_edges[1][l][0]][this_node],
                                                                   added_edges[1][l][1])
            for i in range(n):
                if i != this_node:
                    amount = distance_matrix[i][added_edges[1][l][0]] + distance_matrix[added_edges[1][l][0]][this_node]
                    distance_matrix[i][this_node] = min(distance_matrix[i][this_node], amount)

        added_edges = deleted_node_output[this_node]
        distance_matrix = add_node(this_node, added_edges, distance_matrix, added)
    elif query[0] == 2:
        if distance_matrix[query[1]][query[2]] != max_int:
            answers.append(distance_matrix[query[1]][query[2]])
        else:
            answers.append(-1)

answers.reverse()

for answer in answers:
    print(answer)
