def selection(com):
	n = len(com)
	for i in range(n):
		min_index = i
		for j in range(i+1, n):
			if com[j] < com[min_index]:
				min_index = j
		com[i], com[min_index] = com[min_index], com[i]
    
	print("\nSORTED SALARIES (SELECTION SORT):", com)
    
	print("TOP 5 HIGHEST SALARIES:")
	for salary in range(n-1, n-6,-1):
		print(com[salary])

	
def bubble(com):
	n = len(com)
	for i in range(n):
		for j in range(0, n - i - 1):
			if com[j] > com[j + 1]:
				com[j], com[j + 1] = com[j + 1], com[j]
    
	print("\nSORTED SALARIES (BUBBLE SORT):", com)
    
	print("TOP 5 HIGHEST SALARIES:")
	for salary in range(n-1, n-6,-1):
		print(com[salary])


#-------------------------------------------------------------------------------------------------------------------------------------------
#main program
com = []
n = int(input("ENTER TOTAL NUMBER OF EMPLOYEE: "))

print("\n")
for i in range(n):
		a = float(input(f"ENTER SALLARY FOR EMPLOYEE {i+1}:"))
		com.append(a)

print(com)


while True:
	print("""\n************** E-COMMERCE SYSTEM ****************
	1. SELECTION SORTING
	2. BUBBLE SORTING
	3. EXIT""")
    
	ch = int(input("ENTER YOUR CHOICE: "))
    
	if ch == 1:
		selection(com)
	elif ch == 2:
		bubble(com)	
	elif ch == 3:
		print("THANK YOU!")
		break
	else:
		print("INVALID CHOICE!")


