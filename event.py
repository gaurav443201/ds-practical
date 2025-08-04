from collections import deque

# Global event queue and set of event IDs
event_queue = deque()
event_ids = set()

def add_event():
    event_id = input("ENTER EVENT ID: ")
    if event_id in event_ids:
        print(f"EVENT WITH ID {event_id} ALREADY EXISTS IN QUEUE.")
        return
    description = input("ENTER EVENT DESCRIPTION: ")
    event = {'id': event_id, 'desc': description}
    event_queue.append(event)
    event_ids.add(event_id)
    print(f"ADDED: EVENT(ID={event_id}, DESC={description})")

def process_next_event():
    if not event_queue:
        print("NO EVENTS TO PROCESS.")
        return
    event = event_queue.popleft()
    event_ids.remove(event['id'])
    print(f"PROCESSED: EVENT(ID={event['id']}, DESC={event['desc']})")

def display_pending_events():
    if not event_queue:
        print("NO PENDING EVENTS.")
        return
    print("PENDING EVENTS:")
    for event in event_queue:
        print(f" - EVENT(ID={event['id']}, DESC={event['desc']})")

def cancel_event():
    event_id = input("ENTER EVENT ID TO CANCEL: ")
    if event_id not in event_ids:
        print(f"NO PENDING EVENT WITH ID {event_id} FOUND.")
        return
    global event_queue
    new_queue = deque()
    canceled = False
    while event_queue:
        event = event_queue.popleft()
        if event['id'] == event_id:
            canceled = True
            event_ids.remove(event_id)
            print(f"CANCELED: EVENT(ID={event['id']}, DESC={event['desc']})")
        else:
            new_queue.append(event)
    event_queue = new_queue

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
    choice = input("ENTER YOUR CHOICE: ")
    if choice == '1':
        add_event()
    elif choice == '2':
        process_next_event()
    elif choice == '3':
        display_pending_events()
    elif choice == '4':
        cancel_event()
    elif choice == '5':
        print("THANK YOU FOR USING THE SYSTEM. GOODBYE!")
        break
    else:
        print("INVALID CHOICE. PLEASE ENTER 1-5.")

