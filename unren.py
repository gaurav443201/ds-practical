def make_change(document_state, undo_stack, redo_stack):
    new_text = input("ENTER NEW DOCUMENT TEXT: ")
    undo_stack.append(document_state)
    document_state = new_text
    redo_stack.clear()
    print("\nCHANGE SAVED.")
    return document_state

def undo(document_state, undo_stack, redo_stack):
    if not undo_stack:
        print("\nNOTHING TO UNDO.")
        return document_state
    redo_stack.append(document_state)
    document_state = undo_stack.pop()
    print("\nUNDO SUCCESSFUL.")
    return document_state

def redo(document_state, undo_stack, redo_stack):
    if not redo_stack:
        print("\nNOTHING TO REDO.")
        return document_state
    undo_stack.append(document_state)
    document_state = redo_stack.pop()
    print("\nREDO SUCCESSFUL.")
    return document_state

def display(document_state):
    print("\nCURRENT DOCUMENT STATE:")
    print(f'"{document_state}"')

# ------------------------------------------------------------------------------
# Main Program
print("****************** PRACTICAL NO-01(A-4) TEXT EDITOR ************************")
print("********************* Prepared By : Gaurav B. Navghare **********************")

# Initialize variables
document_state = ""
undo_stack = []
redo_stack = []

while True:
    print("""
************** REAL-TIME TEXT EDITOR SYSTEM ****************
    1. MAKE A CHANGE
    2. UNDO
    3. REDO
    4. DISPLAY DOCUMENT
    5. EXIT
""")
    try:
        ch = int(input("ENTER YOUR CHOICE: "))
    except ValueError:
        print("INVALID INPUT! PLEASE ENTER A NUMBER.")
        continue

    if ch == 1:
        document_state = make_change(document_state, undo_stack, redo_stack)
    elif ch == 2:
        document_state = undo(document_state, undo_stack, redo_stack)
    elif ch == 3:
        document_state = redo(document_state, undo_stack, redo_stack)
    elif ch == 4:
        display(document_state)
    elif ch == 5:
        print("THANK YOU! GOODBYE.")
        break
    else:
        print("INVALID CHOICE! PLEASE TRY AGAIN.")
