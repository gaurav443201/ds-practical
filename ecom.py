def linear(ecom,a):
	key = int(input("ENTER THE ELEMENT WHICH IS TO BE SEARCH :"))
	for i in range(a):
		if key in ecom :
			print("ELEMENT FOUND")
			break
		else:
			print("ELEMENT NOT FOUND")		
			break
def binary(ecom):
	key = int(input("ENTER THE ELEMENT WHICH IS TO BE SEARCHED: "))
    
	low = 0
	high = len(ecom) - 1
    
	while low <= high:
		mid = (low + high) // 2
		print(f"CURRENT MID INDEX IS: {mid}")

		if ecom[mid] == key:
			print("ELEMENT FOUND AT INDEX", mid)
			return mid

		elif ecom[mid] < key:
			print("SEARCHING AT RIGHT SIDE ")
			low = mid + 1

		else:
			print("SEARCHING AT LEFT SIDE")
			high = mid - 1

		print("ELEMENT NOT FOUND")
		return -1






#main program
ecom=[]
n=int(input("ENTER A TOTAL NUMBER OF COSTUMERS:"))

print("\n")
for i in range(n):
	
	a=int(input("ENTER ACCOUNT ID FOR COSTUMER:"))

	ecom.append(a)
	
	
	
print(ecom)

while True:

	print("""**************E-COMMERSE SYSTEM ****************")
	1. LINEAR SEARCH
	2. BINARY SEARCH
	3. EXIT""")
	
	ch= int(input("ENTER YOUR CHOICE:"))
	if (ch==1):
		linear(ecom)
	elif (ch==2):
		binary(ecom)
	elif (ch==3):
		print("THANK YOU !")
		break
	else:
		print("INVALID CHOICE  !")
		
