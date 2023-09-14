import copy
game = [
    [' ', ' ', ' '],
    ['X', ' ', 'O'],
    ['O', ' ', ' ']
]

backup_game = copy.deepcopy(game)

game[0][0] = 'X'
print(backup_game)

