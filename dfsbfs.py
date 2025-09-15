def create(nodes):
    size = len(nodes)
    matrix = [[0] * size for _ in range(size)]
    return matrix

def display(nodes, matrix):
    print("  ", "  ".join(nodes))
    for i in range(len(nodes)):
        print(nodes[i], matrix[i])


n = int(input("Enter number of nodes: "))

nodes = []
for _ in range(n):
    node = input("Enter node name: ")
    nodes.append(node)

matrix = create(nodes)

print("\n **** Adjacency Matrix **** ")
display(nodes, matrix)
