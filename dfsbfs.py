# Graph structures
adj_list = {}
adj_matrix = []
node_names = []

def bfs(start_node):
    visited = set()
    queue = [start_node]

    print("BFS Traversal:")
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    print()

def dfs_util(node, visited):
    print(node, end=' ')
    visited.add(node)
    index = node_names.index(node)
    for i in range(len(node_names)):
        if adj_matrix[index][i] == 1 and node_names[i] not in visited:
            dfs_util(node_names[i], visited)

def dfs(start_node):
    visited = set()
    print("DFS Traversal:")
    dfs_util(start_node, visited)
    print()

# Get number of locations (nodes)
n = int(input("Enter number of locations (nodes): "))

# Get names of nodes
for i in range(n):
    name = input(f"Enter name for location {i + 1}: ")
    node_names.append(name)
    adj_list[name] = []

# Initialize adjacency matrix with zeros
adj_matrix = [[0 for _ in range(n)] for _ in range(n)]

# Create connections between nodes
print("\nEnter connections between locations:")
for i in range(n):
    for j in range(i + 1, n):
        ans = input(f"Is there a route between {node_names[i]} and {node_names[j]}? (yes/no): ").lower()
        if ans == 'yes':
            # Update adjacency list
            adj_list[node_names[i]].append(node_names[j])
            adj_list[node_names[j]].append(node_names[i])
            # Update adjacency matrix
            adj_matrix[i][j] = 1
            adj_matrix[j][i] = 1

# Menu-driven program
while True:
    print("""
*********** GRAPH TRAVERSAL SYSTEM ***********
1. Perform BFS Traversal
2. Perform DFS Traversal
3. View Adjacency List (for BFS)
4. View Adjacency Matrix (for DFS)
5. Exit
""")
    ch = int(input("Enter your choice: "))

    if ch == 1:
        start = input("Enter starting location for BFS: ")
        if start in node_names:
            bfs(start)
        else:
            print("Invalid location!")
    elif ch == 2:
        start = input("Enter starting location for DFS: ")
        if start in node_names:
            dfs(start)
        else:
            print("Invalid location!")
    elif ch == 3:
        print("Adjacency List:")
        for node in adj_list:
            print(f"{node} --> {adj_list[node]}")
    elif ch == 4:
        print("Adjacency Matrix:")
        print("   ", "  ".join(node_names))
        for i in range(n):
            print(f"{node_names[i]}  {'  '.join(map(str, adj_matrix[i]))}")
    elif ch == 5:
        print("Thank you for using the Graph Traversal System. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
