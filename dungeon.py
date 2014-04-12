import random

def roll_dice():
    d6 = random.randint(1, 6)
    return d6

def check_spot(spot):
    if spot in dungeon:
        event_happens = dungeon[spot] - 1000
        print event_text[event_happens]

def game():
    
    # Set variables for new game
    spot = 27
    hp = 3
    key = 0
    talisman = 0
    potion1 = 0
    potion2 = 0
    pole = 0
    
    print 'A new Doomed Soul enters the Deadly Danger Dungeon'
    while hp > 0:        
        
        # Determine which direction to go based on game conditions
        if key == 1 and spot > 1 or spot > 89 and pole == 1:
            # Special case, going backwards
            roll = roll_dice() * -1
            spot = spot + roll
            print spot
            print roll
            check_spot(spot)
        
        else:
            # Normal progression
            roll = roll_dice() 
            spot = spot + roll
            print spot
            print roll
            check_spot(spot)

        if spot > 100:
            print 'You escaped or something'
            hp = 0

dungeon = {1:1001, 6:1002, 8:1003, 10:1004, 11:1005, 13:1006, 16:1006, 19:1005, 21:1004, 23:1003, 24:1003, 29:1005, 30:1005, 35:1005, 40:1007, 43:1003, 44:1008, 45:1003, 48:1013, 52:1005, 54:1015, 55:1015, 56:1005, 58:1008, 63:1009, 66:1016, 69:1005, 71:1005, 73:1005, 75:1010, 79:1010, 83:1011, 84:1011, 85:1011, 86:1011, 88:1011, 102:1014, 104:1012}

event_text = ['Nothing', '1Found the Talisman', '2Used Key', '3Fell into spikes and died', '4Choked on poisonous gas (-1 HP)', '5Fell down deeper into the dungeon (-1 HP)', '6Fell into fire and burned to death', '7Fell into crocodile pit and died', '8Found potion (+2 HP)', '9Found the Key', '10Fell from the ladder and died', '11Escaped!', '12Touched the border and lowered the pole','13Hit by falling boulder (-1 HP)', '14Cave in (-1 HP)', '15Shot by arrows (-1 HP)', '16Used Talisman']


wins = 0
deaths = 0
games = 0

game()
