import random
import time

# --- Board setup ---
snakes = {17: 7, 54: 34, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 99: 78}
ladders = {4: 14, 9: 31, 20: 38, 28: 84, 40: 59, 51: 67, 63: 81, 71: 91}
board_size = 100

# --- Helper functions ---
def roll_dice():
    return random.randint(1, 6)

def apply_snakes_ladders(position):
    if position in ladders:
        print("Ladder! You climb up from", position, "to", ladders[position])
        return ladders[position]
    elif position in snakes:
        print("Snake! You slide down from", position, "to", snakes[position])
        return snakes[position]
    return position

# --- Game setup ---
print("Welcome to Snake and Ladders Game!\n")

while True:
    try:
        num_players = int(input("Enter number of players (2–4): "))
        if 2 <= num_players <= 4:
            break
    except:
        pass
    print("Please enter a valid number between 2 and 4.")

names = []
positions = []
finished = []
for i in range(num_players):
    name = input("Enter name for player " + str(i + 1) + ": ")
    if name.strip() == "":
        name = "Player" + str(i + 1)
    names.append(name)
    positions.append(1)
    finished.append(False)

print("\nSnakes:", snakes)
print("Ladders:", ladders)
input("\nPress Enter to start the game...")

# --- Main game loop ---
ranking = []
current = 0

while len(ranking) < num_players:
    # Skip finished players
    if finished[current]:
        current = (current + 1) % num_players
        continue

    print("\n-----------------------------")
    print(names[current], "'s turn (Position:", positions[current], ")")

    rolls_this_turn = 0

    while True:
        input("Press Enter to throw the dice...")
        roll = roll_dice()
        rolls_this_turn += 1
        print(names[current], "rolled a", roll)

        new_pos = positions[current] + roll
        if new_pos > board_size:
            print("Overshoot! You stay at", positions[current])
        else:
            positions[current] = apply_snakes_ladders(new_pos)

        print("Now at position:", positions[current])

        if positions[current] == board_size:
            finished[current] = True
            ranking.append(names[current])
            print("***", names[current], "finished! Rank:", len(ranking), "***")
            break

        if roll == 6 and rolls_this_turn < 3:
            print("You rolled a 6! Roll again.")
            continue
        elif roll == 6 and rolls_this_turn >= 3:
            print("You rolled 6 three times — turn ends.")
        break

    # Next player's turn
    current = (current + 1) % num_players

# --- Game over ---
print("\n============================")
print("       GAME OVER")
print("============================")

rank_number = 1
while rank_number <= len(ranking):
    print("Rank", rank_number, ":", ranking[rank_number - 1])
    rank_number += 1

i = 0
while i < num_players:
    if not finished[i]:
        print(names[i], "did not finish.")
    i += 1
