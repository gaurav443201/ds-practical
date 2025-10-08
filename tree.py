def is_operator(c):
    return c in ['+', '-', '*', '/', '^']

def construct_expr_tree(prefix_expr):
    index = [0]

    def helper():
        if index[0] >= len(prefix_expr):
            return None

        char = prefix_expr[index[0]]
        index[0] += 1

        node = {'value': char, 'left': None, 'right': None}

        if is_operator(char):
            node['left'] = helper()
            node['right'] = helper()

        return node

    return helper()


def postorder_non_recursive(root):
    if root is None:
        return []

    stack1 = [root]
    stack2 = []

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        if node['left']:
            stack1.append(node['left'])
        if node['right']:
            stack1.append(node['right'])

    return [node['value'] for node in reversed(stack2)]


def delete_tree(root, prefix_expr=None):

    if prefix_expr:
        for ch in prefix_expr:
            print(f"{ch} is deleted")
    if root is None:
        return None
    delete_tree(root['left'])
    delete_tree(root['right'])
    root['left'] = None
    root['right'] = None
    root['value'] = None
    
    return None

	

root = None  # Initially empty tree

while True:
    print("\n**************************** DISPLAY MENU ***********************************")
    print("1. INSERTION")
    print("2. DELETION")
    print("3. DISPLAY")
    print("4. EXIT")
 
    ch = int(input("ENTER THE CHOICE OF OPERATION: "))

    if ch == 1:
        prefix_expr= input("Enter the prefix expression: ").strip()
        root = construct_expr_tree(prefix_expr)
        print("Expression tree constructed.")

    elif ch == 2:
        if root is None:
            print("Tree is already empty.")
        else:
            delete_tree(root)
            root = None
            print("Element deleted")

    elif ch == 3:
        if root is None:
            print("Tree is empty.")
        else:
            print("Postorder traversal (non-recursive):")
            postorder_vals = postorder_non_recursive(root)
            print(' '.join(postorder_vals))

    elif ch == 4:
        print("TERMINATED!!!")
        print("THANK YOU!!!")
        break

    else:
        print("INVALID CHOICE!!!!")
