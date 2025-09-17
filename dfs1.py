# Input nodes
count = int(input("Enter number of nodes: "))
nodes = []
for i in range(count):
    node = input("Enter node name: ")
    nodes.append(node)

size = len(nodes)

# Create adjacency matrix
matrix = []
for i in range(size):
    row = []
    for j in range(size):
        row.append(0)
    matrix.append(row)

# Input edges
edge_count = int(input("Enter number of edges: "))
for k in range(edge_count):
    u = input("Enter first node: ")
    v = input("Enter second node: ")
    if u in nodes and v in nodes:
        i = nodes.index(u)
        j = nodes.index(v)
        matrix[i][j] = 1
        matrix[j][i] = 1  # Undirected graph
    else:
        print("Invalid node name, edge skipped.")


# Display adjacency matrix
print("\n=== Adjacency Matrix ===")
print(" ", " ".join(nodes))
for i in range(size):
    print(nodes[i], " ".join(str(x) for x in matrix[i]))

# DFS function without default argument
def dfs(mat, nodes, start, visited):
    visited.append(start)
    print(nodes[start], end=" ")
    for i in range(len(mat[start])):
        if mat[start][i] == 1 and i not in visited:
            dfs(mat, nodes, i, visited)

# BFS function
def bfs(mat, nodes, start):
    visited = []
    queue = []
    queue.append(start)

    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(nodes[node], end=" ")
            visited.append(node)
            for i in range(len(mat[node])):
                if mat[node][i] == 1 and i not in visited and i not in queue:
                    queue.append(i)

# Start traversal
start_node = input("\nEnter start node for DFS and BFS: ")
if start_node in nodes:
    start_index = nodes.index(start_node)
    print("DFS traversal:")
    dfs(matrix, nodes, start_index, visited=[])
    print("\nBFS traversal:")
    bfs(matrix, nodes, start_index)
else:
    print("Invalid start node.")
