from collections import defaultdict


def read_input(file_name):
    with open(file_name) as input_file:
        graph = defaultdict(list)
        for line in input_file:
            edge = line.rstrip('\n').split('-')
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

    return graph


def is_small(node):
    return node.islower()


def dfs(node, graph, seen, current_path, paths):
    if node == 'end':
        paths.append(current_path)
        return

    if is_small(node):
        seen.add(node)

    for neighbour in graph[node]:
        if neighbour not in seen:
            current_path.append(neighbour)
            dfs(neighbour, graph, seen, current_path, paths)
            current_path.pop()

    if is_small(node):
        seen.remove(node)


def find_path_amount(graph):
    current_node = 'start'
    paths = []

    dfs(current_node, graph, set(), [], paths)

    return len(paths)


if __name__ == '__main__':
    print(find_path_amount(read_input('input.txt')))
