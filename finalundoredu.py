def Type_char(char):
	global text_char , u_stk 
	u_stk.append(text_char)
	text_char += char
	print(text_char)

def undo():
	global text_char
	if u_stk:
		r_stk.append(text_char)
		text_char = u_stk.pop()
		print(text_char)
	else:
		print("NOTHING TO UNDO")		

def redo():
	pass
	
	

#main program
u_stk = []
r_stk = []

text_char = ""


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
        char =  str(input("ENTER CHARACTER: "))
        Type_char(char)
    elif ch == "2":
        undo()
    elif ch == "3":
    	redo()
	elif ch == "4":
    	print("THE CURRENT TEXT PRESENT IN LIST")
    	show(text_char)
    elif ch == "5":
        print("THANK YOU! GOODBYE.")
        break
    else:
        print("INVALID CHOICE! PLEASE ENTER BETWEEN 1 TO 5.")
