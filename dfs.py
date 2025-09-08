# Nodes and mapping
nodes = ['A', 'B', 'C', 'D', 'E']
node_index = {}
for i in range(len(nodes)):
    node_index[nodes[i]] = i

# Adjacency matrix for DFS
adj_matrix = [
    [0,1,1,0,0],  # A
    [0,0,0,1,0],  # B
    [0,0,0,1,1],  # C
    [0,0,0,0,1],  # D
    [0,0,0,0,0]   # E
]

# Adjacency list for BFS
adj_list = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D', 'E'],
    'D': ['E'],
    'E': []
}

# DFS using adjacency matrix
def dfs(start):
    visited = [False] * len(nodes)

    def dfs_util(node_idx):
        visited[node_idx] = True
        print(nodes[node_idx], end=' ')
        for i in range(len(nodes)):
            if adj_matrix[node_idx][i] == 1 and not visited[i]:
                dfs_util(i)

    dfs_util(node_index[start])
    print()

# BFS using adjacency list
from collections import deque
def bfs(start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    print()

print("DFS starting from A:")
dfs('A')

print("BFS starting from A:")
bfs('A')
