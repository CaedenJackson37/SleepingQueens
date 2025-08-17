import random

queen_total = 0
computer_queen_total = 0
player_queens = []
computer_queens = []
last_card_played = None


MainDeck = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Sleeping Potion", "Magic Wand", "Dragon",
            "Joker", "Black Knight", "Red Knight", "Blue Knight", "Green Knight",
            "Cookie King", "Puzzle King", "Hat King", "Fire King", "Bubblegum King",
            "Turtle King", "Chess King", "Tie-Dye King")

Queens = {"Rose Queen":5, "SunFlower Queen":10, "Heart Queen":20, "Cat Queen":15,
          "Dog Queen":15, "Pancake Queen":15, "Ladybug Queen":10, "Rainbow Queen":15,
          "Mermaid Queen":5, "Moon Queen":10, "Peacock Queen":10, "Cake Queen":5}

def draw():
    new_card = random.choice(MainDeck)
    return new_card

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
    if len(computer_queens) < 1:
        print("Sorry, opponent has no Queens to steal.")
    else:
        print(computer_queens)
        queen_steal = input("Which Queen would you like to steal?: ")
        print(f"You have stolen the {queen_steal}")
        player_queens.append(queen_steal)
        computer_queens.remove(queen_steal)
        if "Dragon" in computer_cards:
            computer_queens.append(queen_steal)
            player_queens.remove(queen_steal)
            computer_cards.remove("Dragon")
        else:
            print("Computer has no Dragons")

def obtain_queen():
    queen_name = random.choice(list(Queens.keys()))
    queen_value = Queens[queen_name]

    player_queens.append(queen_name)
    Queens.pop(queen_name)

    global queen_total
    queen_total += queen_value

    print(f"You obtained {queen_name} (worth {queen_value}). Total = {queen_total}")


def sleep_queen():
    if len(computer_queens) < 1:
        print("Computer has no Queens to put to sleep.")
    else:

        print(computer_queens)
        sleeping_queen = input("Which Queen would you like to put to sleep: ")
        if sleeping_queen == "Rose Queen":
            Queens["Rose Queen"] = 0

def awaken_queen():
    print(player_queens)
    awake_queen = input("Which queen would you like to wake up?: ")
    if awake_queen == "Rose Queen":
        Queens["Rose Queen"] = 5


def computer_steal_queen():
    if len(player_queens) < 1:
        print("Sorry, opponent has no Queens to steal.")
    else:
        print(player_queens)
        queen_steal = random.choice(player_queens)
        computer_queens.append(queen_steal)
        player_queens.remove(queen_steal)
        print(f"Computer has stolen the {queen_steal}")
        if "Dragon" in player_cards:
            player_queens.append(queen_steal)
            computer_queens.remove(queen_steal)
            player_cards.remove("Dragon")
        else:
            print("Player has no Dragons")

def computer_obtain_queen():
    queen_name = random.choice(list(Queens.keys()))
    computer_queen_value = Queens[queen_name]

    computer_queens.append(queen_name)
    Queens.pop(queen_name)

    global computer_queen_total
    computer_queen_total += computer_queen_value

    print(f"Computer has obtained {queen_name} (worth {computer_queen_value}). Total = {computer_queen_total}")

def computer_sleep_queen():
    if len(player_queens) < 1:
        print("Player has no Queens to put to sleep.")
    else:
        print(player_queens)
        sleeping_queen = random.choice(player_queens)
        print(f"Computer has put the {sleeping_queen} to sleep.")
        if sleeping_queen == "Rose Queen":
            Queens["Rose Queen"] = 0

def computer_awaken_queen():
    print(computer_queens)
    awake_queen = random.choice(computer_queens)
    if awake_queen == "Rose Queen":
        Queens["Rose Queen"] = 5
def computer_turn():
    computer_place = random.choice(computer_cards)
    try:
        computer_cards.remove(computer_place)
        print(f"Computer has played the {computer_place}")
    except ValueError:
        print(f"{computer_place} could not be found in computer's deck.")
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
    print(player_cards)
    place_card = input("Which card would you like to play?: ")
    try:
        player_cards.remove(place_card)
        print(f"You have played the {place_card}")
    except ValueError:
        print(f"{place_card} could not be found in your deck.")
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
