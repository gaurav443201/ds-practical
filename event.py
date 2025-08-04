

def add(event_id):
    if event_id in queue:
        print(f"EVENT WITH ID {event_id} ALREADY EXISTS IN QUEUE.")
    else:
        queue.append(event_id)
        print(f"ADDED: EVENT ID {event_id}")

def process():
    if not queue:
        print("NO EVENTS TO PROCESS.")
    else:
        event_id = queue.pop(0)
        print(f"PROCESSED: EVENT ID {event_id}")

def display():
    if not queue:
        print("NO PENDING EVENTS.")
    else:
        print("PENDING EVENTS:")
        for event_id in queue:
            print(f" - EVENT ID {event_id}")

def cancel():
    event_id = int(input("ENTER EVENT ID TO CANCEL: "))
    if event_id in queue:
        queue.remove(event_id)
        print(f"CANCELED: EVENT ID {event_id}")
    else:
        print(f"NO PENDING EVENT WITH ID {event_id} FOUND.")

print("WELCOME TO REAL-TIME EVENT PROCESSING SYSTEM")

queue = []

while True:
    print("""
*********** REAL-TIME EVENT PROCESSING SYSTEM ***********
1. ADD AN EVENT
2. PROCESS THE NEXT EVENT
3. DISPLAY PENDING EVENTS
4. CANCEL AN EVENT
5. EXIT
""")
    ch = int(input("ENTER YOUR CHOICE: "))
    
    if ch == 1:
        event_id = int(input("ENTER EVENT ID: "))
        add(event_id)
    elif ch == 2:
        process()
    elif ch == 3:
        display()
    elif ch == 4:
        cancel()
    elif ch == 5:
        print("THANK YOU FOR USING THE SYSTEM. GOODBYE!")
        break
    else:
        print("INVALID CHOICE. PLEASE ENTER A NUMBER BETWEEN 1 AND 5.")
