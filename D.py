n = int(input("Enter number of nodes: "))
nodes = []
for i in range(n):
    node = input(f"Enter node {i+1} name: ")
    nodes.append(node)

#------------------------------------------------------------------------------------------------------

edges = []
print("Enter edges (one per line in format 'node1 node2'). Type 'DONE' when finished:")
while True:
    line = input()
    if line == "DONE":
        break
    parts = line.strip().split()
    if len(parts) == 2:
        edges.append((parts[0], parts[1]))
    else:
        print("Invalid input, enter exactly two nodes or 'DONE'.")

#------------------------------------------------------------------------------------------------------

adjlist = {}
for node in nodes:
    adjlist[node] = []

for u, v in edges:
    adjlist[u].append(v)
    adjlist[v].append(u)

#------------------------------------------------------------------------------------------------------

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

#------------------------------------------------------------------------------------------------------

startnode = input("Enter start node for DFS: ")
if startnode in nodes:
    dfsresult = dfs(startnode)
    print("DFS traversal:", end=" ")
    for i in range(len(dfsresult)):
        print(dfsresult[i], end="")
        if i < len(dfsresult) - 1:
            print(" -> ", end="")
else:
    print("Invalid start node")

