def avg(lib,n):
	sum=0
	for i in lib:
		sum+= i
	avg=sum/n	
	print("\nTOTAL NO. OF BOOKS BORROWED : ", sum)
	print("IT IS AVERAGE FUNCTION FOR BOOK RECORD:",avg)	
	
def high(lib):
	maximum = max(lib)
	print("HIGHEST BOOK BORROWED IS:",maximum)
	
	
def low(lib):
	minimum = min(lib)
	print("LOWEST BOOK BORROWED IS:",minimum)
	 	
def count(lib):
	count=0
	for i in lib:
	 	if(i==0):
	 		count+=1
	print("TOTAL BOOKS COUNT IS:",count)

	 	
def maxFreq(lib):	 	
	i = 0
	print("\n_____________________________")
	print("| book count|frequency count| ")
	print("-----------------------------")

	for ele in lib:
		if lib.index(ele) == i:
			print("|\t ", ele, "|", lib.count(ele), "\t    |")
			print("-----------------------------")
		i += 1  # Increment i each time to check every element index

	for element in lib:	
		if element == max(lib):
			c = lib.count(element)
	print(f"THE MAXIMUM FREQUENCY OF {element} IS {c}")	    

	
# ____________________________________________________________________________________________________________________________#
#main program 
lib=[]
n=int(input("ENTER A TOTAL NUMBER OF STUDENT="))

print("\n")
for i in range(n):
	
	a=int(input("TOTAL NUMBER OF BOOKS BORROWED BY STUDENT:"))

	lib.append(a)
	
	
	
print("lib")

while True:

	print("""************** LIBRARY  RECORD****************")
	1. AVERAGE
	2. HIGHEST
	3. LOWEST
	4. COUNT
	5. FREQUENCY OF BOOK COUNT
	6. EXIT""")
	
	ch=int(input("ENTER YOUR CHOICE:"))
	if (ch==1):
		 avg(lib,n)
	elif (ch==2):
		   high(lib)
	elif (ch==3):
		  low(lib)
	elif (ch==4):
		  count(lib)
	elif (ch==5):
		   maxFreq(lib)
	elif (ch==6):
		print("THANK YOU !")
		break
	else:
		print("INVALID CHOICE  !")
		
	
