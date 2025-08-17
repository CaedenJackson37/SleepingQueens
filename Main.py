import random

queen_total = 0
computer_queen_total = 0
player_queens = []
computer_queens = []
sleeping_queens = []
last_card_played = None


number_cards = [str(n) for n in range (1, 11)] * 4

special_cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Sleeping Potion", "Magic Wand", "Dragon",
            "Joker", "Black Knight", "Red Knight", "Blue Knight", "Green Knight",
            "Cookie King", "Puzzle King", "Hat King", "Fire King", "Bubblegum King",
            "Turtle King", "Chess King", "Tie-Dye King"]

MainDeck = number_cards + special_cards
random.shuffle(MainDeck)

Queens = {"Rose Queen":5, "SunFlower Queen":10, "Heart Queen":20, "Cat Queen":15,
          "Dog Queen":15, "Pancake Queen":15, "Ladybug Queen":10, "Rainbow Queen":15,
          "Mermaid Queen":5, "Moon Queen":10, "Peacock Queen":10, "Cake Queen":5}

def draw():
    if MainDeck:  # make sure deck still has cards
        return MainDeck.pop(0)  # draw the "top" card
    else:
        print("The deck is empty!")
        return None

def player_draw():
    if queen_total < 40:
        while len(player_cards) < 7:
            player_cards.append(draw())
            return player_cards

def computer_draw():
    if computer_queen_total < 40:
        while len(computer_cards) < 7:
            computer_cards.append(draw())
            return computer_cards

def steal_queen():
    if not computer_queens:
        print("Sorry, opponent has no Queens to steal.")
        return

    print("Opponent's Queens:", computer_queens)
    queen_steal = input("Which Queen would you like to steal?: ")

    if queen_steal in computer_queens:
        player_queens.append(queen_steal)
        computer_queens.remove(queen_steal)
        print(f"You have stolen the {queen_steal}")

        if "Dragon" in computer_cards:
            computer_cards.remove("Dragon")
            computer_queens.append(queen_steal)
            player_queens.remove(queen_steal)
            print(f"Computer used a Dragon to defend {queen_steal}!")
    else:
        print("Invalid choice.")

def obtain_queen():
    global queen_total
    if not Queens:
        print("No Queens left to obtain.")
        return

    queen_name = random.choice(list(Queens.keys()))
    queen_value = Queens[queen_name]

    if ("Dog Queen" in player_queens and queen_name == "Cat Queen") or \
            ("Cat Queen" in player_queens and queen_name == "Dog Queen"):
        print("You cannot have both Dog and Cat Queens. Drawing again...")
        return obtain_queen()

    player_queens.append(queen_name)
    queen_total += queen_value
    Queens.pop(queen_name)

    print(f"You obtained {queen_name} (worth {queen_value}). Total = {queen_total}")


def sleep_queen():
    if not computer_queens:
        print("Computer has no Queens to put to sleep.")
        return

    print("Opponent's Queens:", computer_queens)
    sleeping_queen = input("Which Queen would you like to put to sleep?: ")

    if sleeping_queen in computer_queens:
        computer_queens.remove(sleeping_queen)
        Queens[sleeping_queen] = Queens.get(sleeping_queen, 0)  # back to queen pool
        print(f"You put {sleeping_queen} to sleep!")

        if "Magic Wand" in computer_cards:
            computer_cards.remove("Magic Wand")
            computer_queens.append(sleeping_queen)
            Queens.pop(sleeping_queen, None)
            print(f"Computer used Magic Wand to wake {sleeping_queen}!")
    else:
        print("Invalid choice.")

def awaken_queen():
    global sleeping_queens
    if not sleeping_queens:
        print("No Queens are asleep right now.")
        return

    print("Sleeping Queens:", sleeping_queens)
    awake_queen = input("Which queen would you like to wake up?: ")

    if awake_queen in sleeping_queens:
        sleeping_queens.remove(awake_queen)
        player_queens.append(awake_queen)
        print(f"You woke up {awake_queen}!")
    else:
        print("Invalid choice.")


def computer_steal_queen():
    if not player_queens:
        print("Player has no Queens to steal.")
        return

    queen_steal = random.choice(player_queens)
    player_queens.remove(queen_steal)
    computer_queens.append(queen_steal)
    print(f"Computer has stolen the {queen_steal}")

    if "Dragon" in player_cards:
        player_cards.remove("Dragon")
        computer_queens.remove(queen_steal)
        player_queens.append(queen_steal)
        print(f"You used a Dragon to defend {queen_steal}!")

def computer_obtain_queen():
    global computer_queen_total
    if not Queens:
        print("No Queens left to obtain.")
        return

    queen_name = random.choice(list(Queens.keys()))
    queen_value = Queens[queen_name]

    if ("Dog Queen" in computer_queens and queen_name == "Cat Queen") or \
            ("Cat Queen" in computer_queens and queen_name == "Dog Queen"):
        return computer_obtain_queen()

    computer_queens.append(queen_name)
    computer_queen_total += queen_value
    Queens.pop(queen_name)

    print(f"Computer obtained {queen_name} (worth {queen_value}). Total = {computer_queen_total}")

def computer_sleep_queen():
    if not player_queens:
        print("Player has no Queens to put to sleep.")
        return

    sleeping_queen = random.choice(player_queens)
    player_queens.remove(sleeping_queen)
    Queens[sleeping_queen] = Queens.get(sleeping_queen, 0)
    print(f"Computer put {sleeping_queen} to sleep!")

    if "Magic Wand" in player_cards:
        player_cards.remove("Magic Wand")
        player_queens.append(sleeping_queen)
        Queens.pop(sleeping_queen, None)
        print(f"You used Magic Wand to wake {sleeping_queen}!")

def computer_awaken_queen():
    global sleeping_queens

    if not sleeping_queens:
        print("No Queens are asleep right now.")
        return

    awake_queen = random.choice(sleeping_queens)
    sleeping_queens.remove(awake_queen)
    computer_queens.append(awake_queen)
    print(f"Computer woke up {awake_queen}!")


def computer_turn():
    while True:
        computer_place = random.choice(computer_cards)
        if computer_place in computer_cards:
            computer_cards.remove(computer_place)
            print(f"Computer has played the {computer_place}")
            break
        else:
            print(f"{computer_place} could not be found in computer's deck. Try again.")
    if computer_place.endswith("Knight"):
        computer_steal_queen()
    else:
        computer_draw()
    if computer_place == "Sleeping Potion":
        computer_sleep_queen()
    else:
        computer_draw()
    if computer_place == "Magic Wand":
        computer_awaken_queen()
    else:
        computer_draw()
    if computer_place.endswith("King"):
        computer_obtain_queen()
        print(computer_queens)
    else:
        computer_draw()

def player_turn():
    while True:
        print(player_cards)
        place_card = input("Which card would you like to play?: ")
        if place_card in player_cards:
            player_cards.remove(place_card)
            print(f"You have played the {place_card}")
            break
        else:
            print(f"{place_card} could not be found in your deck. Try again.")
    if place_card.endswith("Knight"):
        steal_queen()
    else:
        player_draw()
    if place_card == "Sleeping Potion":
        sleep_queen()
    else:
        player_draw()
    if place_card == "Magic Wand":
        awaken_queen()
    else:
        player_draw()
    if place_card.endswith("King"):
        obtain_queen()
        print(player_queens)
    else:
        player_draw()


player_cards = [draw() for _ in range(7)]
computer_cards = [draw() for _ in range(7)]

while True:
    player_turn()
    computer_turn()
    if queen_total > 39:
        print(f"You have amassed a Queen value of {queen_total}, you win!")
        break
