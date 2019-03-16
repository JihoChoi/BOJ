# TODO Recursive Version
# BFS, DFS

# vertex, edge (node, link), start
N, M, V = map(int, input().split(" "))

links_dict = {new_set: set() for new_set in range(N + 1)}

for _ in range(M):
    a, b = map(int, input().split(" "))
    links_dict[a].add(b)
    links_dict[b].add(a)


# DFS - stack, iterative

def dfs(graph, start):
    visited = []  # foot_prints
    stack = [start]

    while stack:
        top = stack.pop()
        if top not in visited:
            visited.append(top)
            # neighbors = list(graph[top])[::-1]
            neighbors = sorted(graph[top], reverse=True)
            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)
    return visited


# BFS - queue

def bfs(graph, start):
    visited = []  # foot_prints
    queue = [start]

    while queue:
        front = queue.pop(0)
        if front not in visited:
            visited.append(front)
            for neighbor in sorted(graph[front]):
                if neighbor not in visited:
                    queue.append(neighbor)

    return visited


print(*dfs(links_dict, V))
print(*bfs(links_dict, V))

# for node in dfs(links_dict, V):
#     ouput += str(node)
#
# print("")
# for node in bfs(links_dict, V):
#     print(node, end=" ")
