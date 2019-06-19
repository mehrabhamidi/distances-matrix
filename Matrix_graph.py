import queue

dim = int(input())

matrix = []
distances = []
for i in range(dim):
    row = list(map(int, input().split()))
    matrix.append(row)

matrix_dictionary = {}

dimension = dim - 1
for i in range(dim):
    for j in range(dim):
        matrix_dictionary[i * dim + j] = matrix[i][j]

sorted_value = sorted(matrix_dictionary.values())

sorted_list = []

for element in sorted_value:
    for key in matrix_dictionary:
        if element == matrix_dictionary[key]:
            sorted_list.append([key, element])
            del matrix_dictionary[key]
            break

graph = {}
for i in range(dim):
    graph[i] = []


def dijkstra(graph_dictionary, start_node, end_node, visited_node, number_of_visited_node, distances_from_source):
    distances_from_source[start_node] = 0

    priority_queue = queue.Queue()
    priority_queue.put(start_node)

    while priority_queue.qsize() != 0:
        this_node = priority_queue.get()
        if visited_node[this_node] == 0:
            visited_node[this_node] = 1
            number_of_visited_node += 1
            for neighbors in graph_dictionary[this_node]:
                priority_queue.put(neighbors[0])
                new_distance = neighbors[1] + distances_from_source[this_node]
                distances_from_source[neighbors[0]] = min(distances_from_source[neighbors[0]], new_distance)

        else:
            for neighbors in graph_dictionary[this_node]:
                new_distance = neighbors[1] + distances_from_source[neighbors[0]]
                distances_from_source[this_node] = min(distances_from_source[this_node], new_distance)
    return distances_from_source[end_node]


number_of_edges = 0
iterate = True

# building graph bu iterate on distances list in increasinng order
for clause in sorted_list:
    key = clause[0]
    real_distance = clause[1]
    if key < dim:
        i = 0
    else:
        i = int(key / dim)
    j = key - i * dim
    graph_distance = dijkstra(graph, i, j, [0 for _ in range(dim)], 0, [10 ** 14 for _ in range(dim)])

    if i != j:
        if graph_distance < real_distance:
            print('No solution')
            iterate = False
            break
        elif graph_distance > real_distance:
            exist = False
            for inner_clause in graph[i]:
                if clause[0] == j:
                    exist = True
                    break
            if not exist:
                graph[i].append([j, real_distance])
                graph[j].append([i, real_distance])
                number_of_edges += 1

if iterate:
    print(number_of_edges)
    for node in graph:
        for clause in graph[node]:
            print(node + 1, clause[0] + 1, clause[1])
            for search in graph[clause[0]]:
                if search[0] == node:
                    graph[clause[0]].remove(search)
                    break
