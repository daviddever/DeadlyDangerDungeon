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
            
    
    def determine_direction(self):
        # Determine which direction to go based on game conditions
        if (self.player.has_item('key') and self.player.current_spot() > 1) or (self.player.current_spot() > 89 and self.player.pole_down()):
         
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
            if self.player.current_spot() + roll < 1:
                roll = self.player.current_spot() - 1             
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
        self.determine_direction()               
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
    1: Event('Found the Talisman', lambda p: p.add_item('talisman')),
    2: Event('Used Key'),
    3: Event('Fell into spikes and died', lambda p: p.take_damage(-p.current_hp())),
    4: Event('Choked on poisonous gas (-1 HP)', lambda p: p.take_damage(-1)),
    5: Event('Fell down deeper into the dungeon (-1 HP)', lambda p: p.take_damage(-1) and p.move_to_spot(28)),
    6: Event('Fell into fire and burned to death', lambda p: p.take_damage(-p.current_hp())),
    7: Event('Fell into crocodile pint and died', lambda p: p.take_damage(-p.current_hp())),
    8: Event('Found potion (+2 HP)', lambda p: p.add_item('potion1')),
    9: Event('Found the key', lambda p: p.add_item('key')),
    10: Event('Fell from the ladder and died', lambda p: p.take_damage(-p.current_hp())),
    11: Event('Escaped the Deadly Danger Dungeon!'),
    12: Event('Touched the border and lowered the pole', lambda p: p.lower_pole()),
    13: Event('Hit by falling boulder (-1 HP)', lambda p: p.take_damage(-1)),
    14: Event('Cave in (-1 HP)', lambda p: p.take_damage(-1)),
    15: Event('Shot by arrows (-1 HP)', lambda p: p.take_damage(-1)),
    16: Event('Used Talisman'),
    17: Event('Fell down deeper into the dungeon (-1 HP)', lambda p: p.take_damage(-1) and p.move_to_spot(25)),
    18: Event('Fell down deeper into the dungeon (-1 HP)', lambda p: p.take_damage(-1) and p.move_to_spot(49)),
    19: Event('Fell down deeper into the dungeon (-1 HP)', lambda p: p.take_damage(-1) and p.move_to_spot(33)),
    20: Event('Fell down deeper into the dungeon (-1 HP)', lambda p: p.take_damage(-1) and p.move_to_spot(38)),
    21: Event('Fell down deeper into the dungeon (-1 HP)', lambda p: p.take_damage(-1) and p.move_to_spot(100)),
    22: Event('Fell down deeper into the dungeon (-1 HP)', lambda p: p.take_damage(-1) and p.move_to_spot(97)),
    23: Event('Fell down deeper into the dungeon (-1 HP)', lambda p: p.take_damage(-1) and p.move_to_spot(65))     
}

dungeon = {
    1:1, 
    6:2, 
    8:3, 
    10:4, 
    11:5, 
    13:6, 
    16:6, 
    19:17, 
    21:4, 
    23:3, 
    24:3, 
    29:18, 
    30:19, 
    35:20, 
    40:7, 
    43:3, 
    44:8, 
    45:3, 
    48:3,
    52:21, 
    54:15,
    55:15, 
    56:22, 
    58:8, 
    63:9, 
    66:16, 
    69:23, 
    71:23, 
    73:23, 
    75:10, 
    79:10, 
    83:11, 
    84:11, 
    85:11, 
    86:11, 
    88:11, 
    102:14, 
    104:12
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
