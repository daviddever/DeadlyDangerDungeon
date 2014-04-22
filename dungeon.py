import random
import sys

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
            events[dungeon[self.player.current_spot()]].do(self.player)
            
    
    #def determine_direction(self):
        # Determine which direction to go based on game conditions
        #if (self.player.has_item('key') and self.player.current_spot() > 1) or (self.player.current_spot() > 89 and self.player.pole_down()):
         
            # Special case, going backwards
            #self.direction = 0
       
        #else:
            # Normal progression
            #self.direction = 1
   
    def move_spots(self):
        roll = roll_dice()
        #if self.direction == 0:
            # Moving backwards
            #roll = roll * -1
            #if self.player.current_spot() + roll < 1:
                #roll = self.player.current_spot() - 1             
        return roll    

    def check_win(self):
        if self.player.current_spot() in range(83, 89):
            print 'Player escaped!'
            return True
        
    def check_alive(self):
        if self.player.current_hp() > 0:
            return True
        print 'Player is dead'

    def take_turn(self):
        #self.determine_direction()               
        self.player.move_player(self.move_spots())
        self.check_spot()   
  
def roll_dice():
    d6 = random.randint(1, 6)
    return d6

class Event:

    def __init__(self, message, func = None):
        self.message = message
        self.func = func

    def do(self, player):
        if self.func:
            self.func(player)
            print self.message

events = {
    1: Event('Fell down deeper into the dungeon (-1 HP)', lambda p: p.take_damage(-1) and p.move_to_spot(25)),
    2: Event('Fell down deeper into the dungeon (-1 HP)', lambda p: p.take_damage(-1) and p.move_to_spot(8)),
    3: Event('Fell down deeper into the dungeon (-1 HP)', lambda p: p.take_damage(-1) and p.move_to_spot(13)),
    4: Event('Fell into crocodile pint and died', lambda p: p.take_damage(-p.current_hp())),
    5: Event('Fell into spikes and died', lambda p: p.take_damage(-p.current_hp())),
    6: Event('Found potion (+2 HP)', lambda p: p.add_item('potion1')),
    7: Event('Hit by falling boulder (-1 HP)', lambda p: p.take_damage(-1)),
    8: Event('Fell down deeper into the dungeon (-1 HP)', lambda p: p.take_damage(-1) and p.move_to_spot(177)),
    9: Event('Shot by arrows (-1 HP)', lambda p: p.take_damage(-1)),
    10: Event('Fell down deeper into the dungeon (-1 HP)', lambda p: p.take_damage(-1) and p.move_to_spot(174)),
    11: Event('Found potion (+2 HP)', lambda p: p.add_item('potion2')),
    12: Event('Found the key', lambda p: p.add_item('key')),
    13: Event('Fell down deeper into the dungeon (-1 HP)', lambda p: p.take_damage(-1) and p.move_to_spot(64)),
    14: Event('Fell down deeper into the dungeon (-1 HP)', lambda p: p.take_damage(-1) and p.move_to_spot(69)),
    15: Event('Fell down deeper into the dungeon (-1 HP)', lambda p: p.take_damage(-1) and p.move_to_spot(53)),
    16: Event('Choked on poisonous gas (-1 HP)', lambda p: p.take_damage(-1)),
    17: Event('Fell down deeper into the dungeon (-1 HP)', lambda p: p.take_damage(-1) and p.move_to_spot(78)),
    18: Event('Fell into fire and burned to death', lambda p: p.take_damage(-p.current_hp())),
    19: Event('Fell down deeper into the dungeon (-1 HP)', lambda p: p.take_damage(-1) and p.move_to_spot(74)),
    20: Event('Used Key'),
    21: Event('Found the Talisman', lambda p: p.add_item('talisman')),
    22: Event('Fell down deeper into the dungeon (-1 HP)', lambda p: p.take_damage(-1) and p.move_to_spot(128)),
    23: Event('Fell down deeper into the dungeon (-1 HP)', lambda p: p.take_damage(-1) and p.move_to_spot(124)),  
    24: Event('Fell down deeper into the dungeon (-1 HP)', lambda p: p.take_damage(-1) and p.move_to_spot(124)),
    25: Event('Fell down deeper into the dungeon (-1 HP)', lambda p: p.take_damage(-1) and p.move_to_spot(133)),
    26: Event('Fell down deeper into the dungeon (-1 HP)', lambda p: p.take_damage(-1) and p.move_to_spot(137)),
    27: Event('Used Talisman') # This and used key need to be fixed, will only occur if player lands on spot
    28: Event('Fell from the ladder (-1 HP)', lambda p: p.take_damage(-1) and p.move_to_spot(145)),
    29: Event('Fell from the ladder and died', lambda p: p.take_damage(-p.current_hp())),
    30: Event('Escaped the Deadly Danger Dungeon!'),
    31: Event('Cave in (-1 HP)', lambda p: p.take_damage(-1)),
    32: Event('Touched the border and lowered the pole', lambda p: p.lower_pole())
}

dungeon = {
    4: 1, 
    5: 2, 
    10: 3, 
    15: 4, 
    18: 5, 
    19: 6,
    20: 5, 
    23: 7,
    28: 8,
    30: 9,
    31: 9,
    32: 10,
    34: 11,
    39: 12,
    44: 11,
    46: 10,
    50: 8,
    54: 7,
    57: 5,
    58: 6,
    59: 5,
    62: 4,
    67: 13,
    72: 14,
    73: 15, # Come back to this
    79: 5,
    80: 5,
    82: 16,
    84: 17,
    86: 18,
    89: 18,
    91: 19,
    92: 16,
    94: 3,
    96: 20,
    101: 21,
    108: 3,
    110: 16,
    111: 22,
    113: 18,
    113: 18,
    118: 23,
    120: 16,
    122: 5,
    123: 5,
    129: 24, # Come back to this
    130: 25,
    135: 26,
    140: 4,
    143: 5,
    150: 27,
    153: 28,
    155: 28,
    157: 28,
    160: 29,
    161: 29,
    165: 30,
}

wins = 0
deaths = 0
games = 0
finished_games = 0
turn = 0

try:
    games = sys.argv[1]
except:
    games = 1

while finished_games < int(games): 
    # Begin the game
    game = Game()
    while not game.check_win() and game.check_alive():
        game.take_turn()
    finished_games +=1
    if game.check_win() is True:
        wins +=1
    else:
        deaths +=1

print str(games) + ' games played'
print str(deaths) + ' deaths'
print str(wins) + ' wins'
