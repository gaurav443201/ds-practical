def add(customerID, callTime):
    if customerID in queue:
        print(f"CALL FROM CUSTOMER ID {customerID} ALREADY EXISTS IN QUEUE.")
    else:
        queue[customerID] = callTime
        print(f"ADDED: CALL FROM CUSTOMER ID {customerID}, CALL TIME {callTime} MINUTES")

def answer():
    if not queue:
        print("NO CALLS TO ANSWER.")
    else:
        customerID = list(queue.keys())[0] 
        callTime = queue.pop(customerID)
        print(f"ANSWERED CALL: CUSTOMER ID {customerID}, CALL TIME {callTime} MINUTES")

def view():
    if not queue:
        print("NO CALLS IN QUEUE.")
    else:
        print("CALLS CURRENTLY IN QUEUE:")
        for customerID, callTime in queue.items():
            print(f" - CUSTOMER ID: {customerID}, CALL TIME: {callTime} MINUTES")

def cancel():
    customerID = input("ENTER CUSTOMER ID TO CANCEL: ")
    if customerID in queue:
        queue.pop(customerID)
        print(f"CANCELED: CALL FROM CUSTOMER ID {customerID}")
    else:
        print(f"NO CALL FROM CUSTOMER ID {customerID} FOUND IN QUEUE.")

print("WELCOME TO CALL CENTER QUEUE SYSTEM")

queue = {}

while True:
    print("""
*********** CALL CENTER QUEUE SYSTEM ***********
1. ADD A CALL
2. ANSWER THE NEXT CALL
3. VIEW ALL CALLS IN QUEUE
4. CANCEL A CALL
5. EXIT
""")
    ch = int(input("ENTER YOUR CHOICE: "))
    
    if ch == 1:
        customerID = input("ENTER CUSTOMER ID: ")
        callTime = int(input("ENTER CALL TIME (in minutes): "))
        add(customerID, callTime)
    elif ch == 2:
        answer()
    elif ch == 3:
        view()
    elif ch == 4:
        cancel()
    elif ch == 5:
        print("THANK YOU FOR USING THE CALL CENTER QUEUE SYSTEM. GOODBYE!")
        break
    else:
        print("INVALID CHOICE. PLEASE ENTER A NUMBER BETWEEN 1 AND 5.")
