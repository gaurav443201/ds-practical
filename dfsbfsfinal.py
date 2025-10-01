def create_adjacency_matrix(nodes, edges):
    size = len(nodes)
    matrix = [[0] * size for _ in range(size)]
    node_to_index = {}
    for i in range(len(nodes)):
        node_to_index[nodes[i]] = i
    
    for u, v in edges:
        if u in node_to_index and v in node_to_index:
            i = node_to_index[u]
            j = node_to_index[v]
            matrix[i][j] = 1
            matrix[j][i] = 1  # undirected graph
        else:
            print(f"Invalid edge ({u}, {v}) skipped.")
    return matrix

def create_adjacency_list(nodes, edges):
    adj_list = {}
    for i in range(len(nodes)):
        adj_list[nodes[i]] = []
    for u, v in edges:
        if u in adj_list and v in adj_list:
            adj_list[u].append(v)
            adj_list[v].append(u)  # undirected graph
        else:
            print(f"Invalid edge ({u}, {v}) skipped.")
    return adj_list

def dfs(matrix, nodes, start):
    node_to_index = {}
    for i in range(len(nodes)):
        node_to_index[nodes[i]] = i

    visited = [False] * len(nodes)
    stack = []
    result = []

    stack.append(node_to_index[start])

    while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
            result.append(nodes[current])
            for neighbor in range(len(nodes) - 1, -1, -1):
                if matrix[current][neighbor] == 1 and not visited[neighbor]:
                    stack.append(neighbor)
    return result

def bfs(adj_list, start):
    visited = set()
    queue = [start]  # Using list as queue
    result = []

    while queue:
        current = queue.pop(0)  # dequeue
        if current not in visited:
            visited.add(current)
            result.append(current)
            for neighbor in sorted(adj_list[current]):
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
    return result

# Input nodes
n = int(input("Enter number of nodes: "))
nodes = []
for i in range(n):
    node = input(f"Enter node {i+1} name: ")
    nodes.append(node)

# Input edges
edges = []
print("Enter edges (one per line in format 'node1 node2'). Type 'done' when finished:")
while True:
    line = input()
    if line.lower() == "done":
        break
    parts = line.strip().split()
    if len(parts) == 2:
        edges.append((parts[0], parts[1]))
    else:
        print("Invalid input, enter exactly two nodes or 'done'.")

# Build graph representations
matrix = create_adjacency_matrix(nodes, edges)
adj_list = create_adjacency_list(nodes, edges)

print("\nAdjacency Matrix:")
print("  " + "  ".join(nodes))
for i in range(len(nodes)):
    print(nodes[i], matrix[i])

print("\nAdjacency List:")
for i in range(len(nodes)):
    print(f"{nodes[i]}: {adj_list[nodes[i]]}")

start_node = input("\nEnter the starting node for traversal: ")

if start_node not in nodes:
    print("Invalid start node.")
else:
    print("\nDFS (using adjacency matrix):")
    dfs_order = dfs(matrix, nodes, start_node)
    print(" -> ".join(dfs_order))

    print("\nBFS (using adjacency list):")
    bfs_order = bfs(adj_list, start_node)
    print(" -> ".join(bfs_order))
