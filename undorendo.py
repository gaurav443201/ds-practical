def change(doc, u_stk, r_stk):
    new_txt = input("ENTER NEW DOCUMENT TEXT: ")
    u_stk.append(doc)
    doc = new_txt
    r_stk.clear()
    print("\nCHANGE SAVED.")
    return doc

def undo(doc, u_stk, r_stk):
    if len(u_stk) == 0:
        print("\nNOTHING TO UNDO.")
    else:
        r_stk.append(doc)
        doc = u_stk.pop()
        print("\nUNDO SUCCESSFUL.")
    return doc

def redo(doc, u_stk, r_stk):
    if len(r_stk) == 0:
        print("\nNOTHING TO REDO.")
    else:
        u_stk.append(doc)
        doc = r_stk.pop()
        print("\nREDO SUCCESSFUL.")
    return doc

def show(doc):
    print("\nCURRENT DOCUMENT STATE:")
    print(f'"{doc}"')

# ------------------------------------------------------------------------------
# Main Program
print("****************** PRACTICAL NO-01(B-1) TEXT EDITOR ************************")
print("********************* Prepared By : Gaurav B. Navghare **********************")

doc = ""
u_stk = []
r_stk = []

while True:
    print("""
************** REAL-TIME TEXT EDITOR SYSTEM ****************
    1. MAKE A CHANGE
    2. UNDO
    3. REDO
    4. DISPLAY DOCUMENT
    5. EXIT
""")
    ch = input("ENTER YOUR CHOICE: ")

    if ch == "1":
        doc = change(doc, u_stk, r_stk)
    elif ch == "2":
        doc = undo(doc, u_stk, r_stk)
    elif ch == "3":
        doc = redo(doc, u_stk, r_stk)
    elif ch == "4":
        show(doc)
    elif ch == "5":
        print("THANK YOU! GOODBYE.")
        break
    else:
        print("INVALID CHOICE! PLEASE ENTER BETWEEN 1 TO 5.")

