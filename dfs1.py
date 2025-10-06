# Initialize global variables
nodes = []
edges = []
adjlist = {}

def add_nodes():
    global nodes, adjlist
    n = int(input("Enter number of nodes: "))
    nodes = []
    for i in range(n):
        node = input(f"Enter node {i+1} name: ")
        nodes.append(node)
    
    # Reinitialize adjacency list
    adjlist = {}
    for node in nodes:
        adjlist[node] = []
    
    print(f"Added {n} nodes successfully!")

def add_connections():
    global edges, adjlist
    if not nodes:
        print("Please add nodes first!")
        return
    
    edges = []
    print("Enter edges (one per line in format 'node1 node2'). Type 'DONE' when finished:")
    while True:
        line = input()
        if line == "DONE":
            break
        parts = line.strip().split()
        if len(parts) == 2:
            if parts[0] in nodes and parts[1] in nodes:
                edges.append((parts[0], parts[1]))
            else:
                print("Error: One or both nodes not found in node list!")
        else:
            print("Invalid input, enter exactly two nodes or 'DONE'.")
    
    # Rebuild adjacency list
    for node in nodes:
        adjlist[node] = []
    
    for u, v in edges:
        adjlist[u].append(v)
        adjlist[v].append(u)
    
    print(f"Added {len(edges)} connections successfully!")

def display_adjacency_matrix_dfs():
    if not nodes:
        print("No nodes added yet!")
        return
    
    print("\nAdjacency Matrix for DFS:")
    print("    " + "  ".join(nodes))
    for node in nodes:
        row = [node]
        for neighbor in nodes:
            if neighbor in adjlist[node]:
                row.append("1")
            else:
                row.append("0")
        print("  ".join(row))

def display_dfs_traversal():
    if not nodes:
        print("No nodes added yet!")
        return
    
    startnode = input("Enter start node for DFS traversal: ")
    if startnode not in nodes:
        print("Invalid start node!")
        return
    
    def dfs(start):
        visited = set()
        stack = [start]
        result = []

        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                result.append(current)
                for neighbor in sorted(adjlist[current], reverse=True):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return result

    dfsresult = dfs(startnode)
    print("DFS traversal:", end=" ")
    for i in range(len(dfsresult)):
        print(dfsresult[i], end="")
        if i < len(dfsresult) - 1:
            print(" -> ", end="")
    print()

def display_adjacency_matrix_bfs():
    if not nodes:
        print("No nodes added yet!")
        return
    
    print("\nAdjacency Matrix for BFS:")
    print("    " + "  ".join(nodes))
    for node in nodes:
        row = [node]
        for neighbor in nodes:
            if neighbor in adjlist[node]:
                row.append("1")
            else:
                row.append("0")
        print("  ".join(row))

def display_bfs_traversal():
    if not nodes:
        print("No nodes added yet!")
        return
    
    startnode = input("Enter start node for BFS traversal: ")
    if startnode not in nodes:
        print("Invalid start node!")
        return
    
    def bfs(start):
        visited = set()
        queue = [start]
        result = []

        while queue:
            current = queue.pop(0)
            if current not in visited:
                visited.add(current)
                result.append(current)
                for neighbor in sorted(adjlist[current]):
                    if neighbor not in visited and neighbor not in queue:
                        queue.append(neighbor)
        return result

    bfsresult = bfs(startnode)
    print("BFS traversal:", end=" ")
    for i in range(len(bfsresult)):
        print(bfsresult[i], end="")
        if i < len(bfsresult) - 1:
            print(" -> ", end="")
    print()

# Main program loop
while True:
    print("""
GRAPH MENU:
1. ADD NODES
2. ADD CONNECTIONS
3. Display adjacency matrix for DFS
4. Display DFS Traversal
5. Display adjacency matrix for BFS
6. Display BFS Traversal
7. EXIT
""")
    
    choice = input("Enter your choice (1-7): ")
    
    if choice == '1':
        add_nodes()
    elif choice == '2':
        add_connections()
    elif choice == '3':
        display_adjacency_matrix_dfs()
    elif choice == '4':
        display_dfs_traversal()
    elif choice == '5':
        display_adjacency_matrix_bfs()
    elif choice == '6':
        display_bfs_traversal()
    elif choice == '7':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1-7.")
