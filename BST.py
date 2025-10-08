def insert(root, node):
    if root is None:
        return node

    if node["value"] < root["value"]:
        root["left"] = insert(root["left"], node)
    elif node["value"] > root["value"]:
        root["right"] = insert(root["right"], node)
    else:
        print("Key already exists!")
    return root


def search(root, key):
    if root is None:
        return False
    if key == root["value"]:
        return True
    elif key < root["value"]:
        return search(root["left"], key)
    else:
        return search(root["right"], key)


def find_min_node(root):
    current = root
    while current and current["left"] is not None:
        current = current["left"]
    return current


def delete(root, key):
    if root is None:
        return root

    if key < root["value"]:
        root["left"] = delete(root["left"], key)
    elif key > root["value"]:
        root["right"] = delete(root["right"], key)
    else:
        # Node found
        if root["left"] is None:
            return root["right"]
        elif root["right"] is None:
            return root["left"]

        min_node = find_min_node(root["right"])
        root["value"] = min_node["value"]
        root["right"] = delete(root["right"], min_node["value"])

    return root


def inorder_display(root):
    if root is not None:
        inorder_display(root["left"])
        print(root["value"], end=" ")
        inorder_display(root["right"])


# MAIN PROGRAM
root = None  # Empty tree initially

while True:
    print("\n**************************** DISPLAY MENU ***********************************")
    print("1. INSERTION")
    print("2. DELETION")
    print("3. DISPLAY")
    print("4. SEARCH")
    print("5. EXIT")

    ch = int(input("ENTER YOUR CHOICE: "))

    if ch == 1:
        n = int(input("How many numbers do you want to insert? "))
        for _ in range(n):
            key = int(input("Enter value to insert: "))
            new_node = {"value": key, "left": None, "right": None}
            root = insert(root, new_node)

    elif ch == 2:
        key = int(input("Enter value to delete: "))
        root = delete(root, key)

    elif ch == 3:
        if root is None:
            print("Tree is empty.")
        else:
            print("BST in inorder: ", end="")
            inorder_display(root)
            print()

    elif ch == 4:
        key = int(input("Enter value to search: "))
        found = search(root, key)
        if found:
            print(f"{key} found in the BST.")
        else:
            print(f"{key} NOT found in the BST.")

    elif ch == 5:
        print("THANK YOU!!!")
        break

    else:
        print("INVALID CHOICE!!!!")
