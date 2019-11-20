# Overview of Iterators vs Generators in Python

        # generators
class InfiniteLineup:
    def __init__(self, players):
        self.players = players

    def lineup(self):
        lineup_max = len(self.players) # bring in total count of players
        idx = 0

        while True: # continue until told to stop (while loop)
            if idx < lineup_max:
                yield self.players[idx]             # yield to generator obj => creates next beh
            else:
                idx = 0
                yield self.players[idx]          # yield => creates generator obj ... no next needed

            idx += 1
    
    def __repr__(self):
        return f'<InfiniteLineup({self.players})'

    def __str__(self):
        return f'InfniteLineup with the players: {self.players}'


astros = [
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

full_lineup = InfiniteLineup(astros)
astros_lineup = full_lineup.lineup()           # create an instance

print(next(astros_lineup)) # => springer 
print(next(astros_lineup)) # => bregman
print(next(astros_lineup)) # => altuve
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))

print(repr(astros_lineup))
print(str(astros_lineup))

#   notes:
# doesnt print data
# => <generator object InfiniteLineup.lineup at 0x000001867CAEFCC8>
# => <generator object InfiniteLineup.lineup at 0x000001867CAEFCC8>
# generator used more for making ur own custom behavior since easier to read