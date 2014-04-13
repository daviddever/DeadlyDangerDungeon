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

    def move_to_spot(self, spot):
        self.spot = spot

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
            event_happens = dungeon[self.player.current_spot()] - 1000
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
        self.player.move_player(self.move_spots())
        self.check_spot()   
  
def roll_dice():
    d6 = random.randint(1, 6)
    return d6

class Event:

    def __init__(self, player, message, func = None):
        self.message = message
        self.player = player
        self.func = func

    def do(self):
        self.func(self.player)

events = {
    1: Event(player, 'Found the Talisman', lambda p: p.add_item('talisman'))
    2: Event(player, 'Used Key')
    3: Event(player, 'Fell into spikes and died', lambda p: p.take_damage(-p.current_hp()))
    4: Event(player, 'Choked on poisonous gas (-1 HP)', lambda p: p.take_damage(-1))
    5: Event(player, 'Fell down deeper into the dungeon (-1 HP)', lambda p: p.take_damage(-1) and p.move_to_spot(1))
    6: Event(player, 'Fell into fire and burned to death', lambda p: p.take_damage(-p.current_hp()))
    7: Event(player, 'Fell into crocodile pint and died', lambda p: p.take_damage(-p.current_hp()))
    8: Event(player, 'Found potion (+2 HP)', lambda p: p.add_item('potion1'))
    9: Event(player, 'Found the key', lambda p: p.add_item('key'))
    10: Event(player, 'Fell from the ladder and died', lambda p: p.take_damage(-p.current_hp()))
    11: Event(player, 'Escaped the Deadly Danger Dungeon!')
    12: Evemt(player, 'Touched the border and lowered the pole', lambda p: p.lower_pole())
    13: Event(player, 'Hit by falling boulder (-1 HP)', lambda p: p.take_damage(-1))
    14: Event(player, 'Cave in (-1 HP)', lambda p: p.take_damage(-1))
    15: Event(player, 'Shot by arrows (-1 HP)', lambda p: p.take_damage(-1))
    16: Event(player, 'Used Talisman')
}

dungeon = {1:1001, 6:1002, 8:1003, 10:1004, 11:1005, 13:1006, 16:1006, 19:1005, 21:1004, 23:1003, 24:1003, 29:1005, 30:1005, 35:1005, 40:1007, 43:1003, 44:1008, 45:1003, 48:1013, 52:1005, 54:1015, 55:1015, 56:1005, 58:1008, 63:1009, 66:1016, 69:1005, 71:1005, 73:1005, 75:1010, 79:1010, 83:1011, 84:1011, 85:1011, 86:1011, 88:1011, 102:1014, 104:1012}

wins = 0
deaths = 0
games = 0

# Begin the game
game = Game()
while not game.check_win() and game.check_alive():
    game.take_turn()
