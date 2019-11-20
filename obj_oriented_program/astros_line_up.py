# How to Build a Custom Iterator Class in Python
class Lineup: # infinite lineup
    def __init__(self, players):
        self.players = players

    def __iter__(self):
        self.n = 0 # counter variable to keep track of where we are in the line up (index) # n = 0 first time
        return self

    def __next__(self):
        if self.n < (len(self.players) - 1): # is n less than length of the list... need -1 not length of list but want the value of index of the last element (tucker which is 8) -> comparing index with last index so use lens -1 => index number of last element
            player =  self.players[self.n] # grab the player
            self.n += 1 # makes it iterable to move down the line
            return player
        elif self.n == (len(self.players) - 1):
            player = self.players[self.n]
            self.n = 0 # starts counter over 
            return player
        
astros = [  # list of strings 
  'Springer',
  'Bregman',
  'Altuve',
  'Correa',
  'Reddick',
  'Gonzalez',
  'McCann',
  'Davis',
  'Tucker'
]

astros_lineup = Lineup(astros)
process = iter(astros_lineup)

print(next(process)) 
print(next(process))
print(next(process)) 
print(next(process))
print(next(process)) 
print(next(process))
print(next(process)) 
print(next(process))
print(next(process)) 
print(next(process))
print(next(process)) 
print(next(process))
print(next(process)) 
print(next(process))
print(next(process)) 
print(next(process))
print(next(process)) 
print(next(process))
print(next(process)) 
print(next(process))
print(next(process)) 
print(next(process))
print(next(process)) 
print(next(process))
 
 """ returned: 
Springer
Bregman
Altuve
Correa
Reddick
Gonzalez
McCann
Davis
Tucker
Springer
Bregman
Altuve
Correa
Reddick
Gonzalez
McCann
Davis
Tucker
Springer
Bregman
Altuve
Correa
Reddick
Gonzalez
"""