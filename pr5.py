queue = []

def is_valid_int(s):
    return s.isdigit()  # Only digits, positive integers

def add(event_id):
    exists = False
    for e in queue:
        if e == event_id:
            exists = True
            break
    if exists:
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
    event_id_str = input("ENTER EVENT ID TO CANCEL: ")
    if not is_valid_int(event_id_str):
        print("INVALID EVENT ID. PLEASE ENTER A POSITIVE INTEGER.")
    else:
        event_id = int(event_id_str)
        found = False
        for i in range(len(queue)):
            if queue[i] == event_id:
                found = True
                del queue[i]
                print(f"CANCELED: EVENT ID {event_id}")
                break
        if not found:
            print(f"NO PENDING EVENT WITH ID {event_id} FOUND.")

print("WELCOME TO REAL-TIME EVENT PROCESSING SYSTEM")

while True:
    print("""
*********** REAL-TIME EVENT PROCESSING SYSTEM ***********
1. ADD AN EVENT
2. PROCESS THE NEXT EVENT
3. DISPLAY PENDING EVENTS
4. CANCEL AN EVENT
5. EXIT
""")
    ch_str = input("ENTER YOUR CHOICE: ")
    if not is_valid_int(ch_str):
        print("INVALID CHOICE. PLEASE ENTER A NUMBER BETWEEN 1 AND 5.")
    else:
        ch = int(ch_str)
        if ch == 1:
            event_id_str = input("ENTER EVENT ID: ")
            if not is_valid_int(event_id_str):
                print("INVALID EVENT ID. PLEASE ENTER A POSITIVE INTEGER.")
            else:
                event_id = int(event_id_str)
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
