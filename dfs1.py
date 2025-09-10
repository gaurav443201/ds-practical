def create_adjacency_matrix(nodes, edges):
    size = len(nodes)
    matrix = [[0] * size for _ in range(size)]
    
    for edge in edges:
        i = nodes.index(edge[0])
        j = nodes.index(edge[1])
        matrix[i][j] = 1
        matrix[j][i] = 1  # For undirected graph
    
    return matrix

def create_adjacency_list(nodes, edges):
    adj_list = {}
    for node in nodes:
        adj_list[node] = []
    
    for edge in edges:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])  # For undirected graph
    
    return adj_list

def display_matrix(nodes, matrix):
    print("   ", " ".join(nodes))
    for i in range(len(nodes)):
        print(nodes[i], " ", " ".join(str(x) for x in matrix[i]))

def display_list(adj_list):
    for node, neighbors in adj_list.items():
        print(f"{node}: {', '.join(neighbors)}")

def bfs(adj_list, start):
    visited = []
    queue = [start]
    
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            for neighbor in adj_list[node]:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
    
    return visited

def dfs(adj_matrix, nodes, start):
    visited = []
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            node_index = nodes.index(node)
            for i in range(len(nodes)-1, -1, -1):
                if adj_matrix[node_index][i] == 1 and nodes[i] not in visited:
                    stack.append(nodes[i])
    
    return visited

# Main program
print("WELCOME TO GRAPH TRAVERSAL SYSTEM")
print("==================================")

nodes = []
edges = []

n = int(input("ENTER NUMBER OF NODES: "))
for i in range(n):
    node = input(f"ENTER NODE {i+1} NAME: ")
    nodes.append(node)

print("\nENTER EDGES (FORMAT: A B). ENTER 'DONE' WHEN FINISHED:")
while True:
    edge_input = input("EDGE: ")
    if edge_input.upper() == 'DONE':
        break
    edge = edge_input.split()
    if len(edge) == 2 and edge[0] in nodes and edge[1] in nodes:
        edges.append((edge[0], edge[1]))
    else:
        print("INVALID EDGE. PLEASE ENTER TWO VALID NODE NAMES.")

adj_matrix = create_adjacency_matrix(nodes, edges)
adj_list = create_adjacency_list(nodes, edges)

while True:
    print("\n============= GRAPH TRAVERSAL SYSTEM =============")
    print("1. DISPLAY ADJACENCY MATRIX")
    print("2. DISPLAY ADJACENCY LIST")
    print("3. PERFORM BFS TRAVERSAL")
    print("4. PERFORM DFS TRAVERSAL")
    print("5. EXIT")
    print("==================================================")
    
    choice = int(input("ENTER YOUR CHOICE: "))
    
    if choice == 1:
        print("\nADJACENCY MATRIX:")
        display_matrix(nodes, adj_matrix)
    
    elif choice == 2:
        print("\nADJACENCY LIST:")
        display_list(adj_list)
    
    elif choice == 3:
        start_node = input("ENTER STARTING NODE FOR BFS: ")
        if start_node in nodes:
            result = bfs(adj_list, start_node)
            print(f"BFS TRAVERSAL: {' -> '.join(result)}")
        else:
            print("INVALID NODE. PLEASE ENTER A VALID NODE NAME.")
    
    elif choice == 4:
        start_node = input("ENTER STARTING NODE FOR DFS: ")
        if start_node in nodes:
            result = dfs(adj_matrix, nodes, start_node)
            print(f"DFS TRAVERSAL: {' -> '.join(result)}")
        else:
            print("INVALID NODE. PLEASE ENTER A VALID NODE NAME.")
    
    elif choice == 5:
        print("THANK YOU FOR USING THE GRAPH TRAVERSAL SYSTEM. GOODBYE!")
        break
    
    else:
        print("INVALID CHOICE. PLEASE ENTER A NUMBER BETWEEN 1 AND 5.")
