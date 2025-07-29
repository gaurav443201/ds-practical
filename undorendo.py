# ---------------------------- UNDO/REDO TEXT EDITOR -----------------------------

# Global variables
document_state = ""
undo_stack = []
redo_stack = []

def make_change():
    global document_state, undo_stack, redo_stack
    new_text = input("ENTER NEW DOCUMENT TEXT: ")
    undo_stack.append(document_state)
    document_state = new_text
    redo_stack.clear()
    print("\nCHANGE SAVED.")

def undo():
    global document_state, undo_stack, redo_stack
    if not undo_stack:
        print("\nNOTHING TO UNDO.")
        return
    redo_stack.append(document_state)
    document_state = undo_stack.pop()
    print("\nUNDO SUCCESSFUL.")

def redo():
    global document_state, undo_stack, redo_stack
    if not redo_stack:
        print("\nNOTHING TO REDO.")
        return
    undo_stack.append(document_state)
    document_state = redo_stack.pop()
    print("\nREDO SUCCESSFUL.")

def display():
    global document_state
    print("\nCURRENT DOCUMENT STATE:")
    print(f'"{document_state}"')

# ------------------------------------------------------------------------------
# Main Program
print("****************** PRACTICAL NO-01(A-4) TEXT EDITOR ************************")
print("********************* Prepared By : Gaurav B. Navghare **********************")

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
        make_change()
    elif ch == 2:
        undo()
    elif ch == 3:
        redo()
    elif ch == 4:
        display()
    elif ch == 5:
        print("THANK YOU! GOODBYE.")
        break
    else:
        print("INVALID CHOICE! PLEASE TRY AGAIN.")
