import random

class Player:

    def __init__(self):
        self.spot = 27
        self.hp = 3
        self.key = 0
        self.talisman = 0
        self.potion1 = 0
        self.potion2 = 0
        self.pole = 0

    def move_player(self, spots):
        self.spot += spots

    def take_damage(self, dmg):
        self.hp += dmg

    def add_item(self, item):
        setattr(self, item, True)
        if item.startswith('potion'):
            self.hp += 2

    def lower_pole(self):
        self.pole = True
   
    def has_item(self, item):
        return getattr(self, item)

    def pole_down(self):
        return self.pole

    def current_spot(self):
        return self.spot

    def current_hp(self):
        return self.hp

class Game:

    def __init__(self):    
        print 'A new Doomed Soul enters the Deadly Danger Dungeon'
        self.player = Player()

    def check_spot(self):
        if self.player.current_spot() in dungeon:
            event_happens = dungeon[spot] - 1000
            print event_text[event_happens]
    
    def determine_direction(self):
        # Determine which direction to go based on game conditions
        if self.player.has_item('key') == True and self.player.current_spot() > 1 or self.player.current_spot() > 89 and self.player.pole_down() == True:
            # Special case, going backwards
            self.direction = 0
       
        else:
            # Normal progression
            self.direction = 1
   
    def move_spots(self):
        roll = roll_dice()
        if self.direction == 0:
            # Moving backwards
            roll = roll * -1
        return roll    

    def check_win(self):
        if self.player.current_spot() > 100:
            return True

    def check_alive(self):
        if self.player.current_hp() > 0:
            return True

    def take_turn(self):
        self.determine_direction()
        self.move_spots()
        self.check_spot()   
  
def roll_dice():
    d6 = random.randint(1, 6)
    return d6

dungeon = {1:1001, 6:1002, 8:1003, 10:1004, 11:1005, 13:1006, 16:1006, 19:1005, 21:1004, 23:1003, 24:1003, 29:1005, 30:1005, 35:1005, 40:1007, 43:1003, 44:1008, 45:1003, 48:1013, 52:1005, 54:1015, 55:1015, 56:1005, 58:1008, 63:1009, 66:1016, 69:1005, 71:1005, 73:1005, 75:1010, 79:1010, 83:1011, 84:1011, 85:1011, 86:1011, 88:1011, 102:1014, 104:1012}

event_text = ['Nothing', '1Found the Talisman', '2Used Key', '3Fell into spikes and died', '4Choked on poisonous gas (-1 HP)', '5Fell down deeper into the dungeon (-1 HP)', '6Fell into fire and burned to death', '7Fell into crocodile pit and died', '8Found potion (+2 HP)', '9Found the Key', '10Fell from the ladder and died', '11Escaped!', '12Touched the border and lowered the pole','13Hit by falling boulder (-1 HP)', '14Cave in (-1 HP)', '15Shot by arrows (-1 HP)', '16Used Talisman']

wins = 0
deaths = 0
games = 0

# Begin the game
game = Game()
while not game.check_win() and game.check_alive():
    game.take_turn()
