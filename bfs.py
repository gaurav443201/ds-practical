# Input nodes
n = int(input("Enter number of nodes: "))
nodes = []
for i in range(n):
    node = input(f"Enter node {i+1} name: ")
    nodes.append(node)

#------------------------------------------------------------------------------------------------------
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

#------------------------------------------------------------------------------------------------------
# Create adjacency list
adjlist = {}
for node in nodes:
    adjlist[node] = []

for u, v in edges:
    adjlist[u].append(v)
    adjlist[v].append(u)

#------------------------------------------------------------------------------------------------------
# BFS function
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

#------------------------------------------------------------------------------------------------------
# Get start node and perform BFS
startnode = input("Enter start node for BFS: ")
if startnode in nodes:
    bfsresult = bfs(startnode)
    print("BFS traversal:", end=" ")
    for i in range(len(bfsresult)):
        print(bfsresult[i], end="")
        if i < len(bfsresult) - 1:
            print(" -> ", end="")
else:
    print("Invalid start node")
