hash_table = []
for _ in range(10):
    hash_table.append([])

def hash_function(key):
    return key % 10

def insert(key, value):
    index = hash_function(key)
    for item in hash_table[index]:
        if item[0] == key:
            item[1] = value
            print(f"Updated key {key} with value '{value}' at index {index}")
            return
    hash_table[index].append([key, value])
    print(f"Inserted key {key} with value '{value}' at index {index}")

def search(key):
    index = hash_function(key)
    for item in hash_table[index]:
        if item[0] == key:
            print(f"Key {key} found with value '{item[1]}' at index {index}")
            return
    print(f"Key {key} not found")

def delete(key):
    index = hash_function(key)
    i = 0
    while i < len(hash_table[index]):
        if hash_table[index][i][0] == key:
            hash_table[index].pop(i)
            print(f"Key {key} deleted from index {index}")
            return
        i += 1
    print(f"Key {key} not found for deletion")

def display():
    print("\nCurrent Hash Table:")
    for i in range(len(hash_table)):
        print(f"Index {i}: {hash_table[i]}")

print("******** HASH TABLE USING DIVISION METHOD ********")

while True:
    print("""
1. Insert key-value
2. Search key
3. Delete key
4. Display table
5. Exit
""")
    choice = int(input("Enter choice: "))

    if choice == 1:
        k = int(input("Enter key (integer): "))
        v = input("Enter value: ")
        insert(k, v)
    elif choice == 2:
        k = int(input("Enter key to search: "))
        search(k)
    elif choice == 3:
        k = int(input("Enter key to delete: "))
        delete(k)
    elif choice == 4:
        display()
    elif choice == 5:
        print("Thank you!")
        break
    else:
        print("Invalid choice! Try again.")
