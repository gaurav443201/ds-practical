def linear(ecom):
    key = int(input("ENTER THE ELEMENT WHICH IS TO BE SEARCHED: "))
    if key in ecom:
        print("ELEMENT FOUND")
    else:
        print("ELEMENT NOT FOUND")


def binary(ecom):
    key = int(input("ENTER THE ELEMENT WHICH IS TO BE SEARCHED: "))
    
    low = 0
    high = len(ecom) - 1
    
    while low <= high:
        mid = (low + high) // 2
        print(f"CURRENT MID INDEX IS: {mid}")

        if ecom[mid] == key:
            print("ELEMENT FOUND AT INDEX", mid)
            return
        elif ecom[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    print("ELEMENT NOT FOUND")


# Main program
ecom = []
n = int(input("ENTER TOTAL NUMBER OF CUSTOMERS: "))

for i in range(n):
    a = int(input("ENTER ACCOUNT ID FOR CUSTOMER: "))
    ecom.append(a)

ecom.sort()
print("SORTED ACCOUNT IDS:", ecom)

while True:
    print("""\n************** E-COMMERCE SYSTEM ****************
    1. LINEAR SEARCH
    2. BINARY SEARCH
    3. EXIT""")
    
    ch = int(input("ENTER YOUR CHOICE: "))
    
    if ch == 1:
        linear(ecom)
    elif ch == 2:
        binary(ecom)
    elif ch == 3:
        print("THANK YOU!")
        break
    else:
        print("INVALID CHOICE!")

		
