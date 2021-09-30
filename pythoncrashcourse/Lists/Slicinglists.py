# Slicing trough the lists

players = ['michael', 'marting', 'pipin', 'frodo', 'Argon', 'loegolas']

for player in players[:3]:
    
    print("the best players r , " +player.title()+ "!")


print(players[0:4])
print(players[1:4])
print(players[:4])
print(players[4:])
print(players[2:])

# copying the lists
my_games = ['a','b','c','d']
games = my_games[:]
my_games.append('e')
games.append('f')
print(my_games)
print(games)