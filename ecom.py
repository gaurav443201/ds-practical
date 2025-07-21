def linear(ecom):
	key = int(input("ENTER THE ELEMENT WHICH IS TO BE SEARCH :"))
	for i in range(len(ecom)):
		if key == ecom[i]:
			print("ELEMENT FOUND")
		else:
			print("ELEMENT NOT FOUND")		
			break	
def binary(ecom):
	pass	









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
		
