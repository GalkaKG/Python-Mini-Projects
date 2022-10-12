def turn_players(players_data, counter):
    if counter % 2 == 0:
        return players_data[1][0], players_data[1][1]
    else:
        return players_data[0][0], players_data[0][1]


def is_valid_position(position):
    return 1 <= position <= 9 and type(position) == int


def check_if_wins(positions, curr_sign):
    if positions[1] == curr_sign and positions[2] == curr_sign and positions[3] == curr_sign or positions[4] \
            == curr_sign and positions[5] == curr_sign and positions[6] == curr_sign or positions[7] == curr_sign \
            and positions[8] == curr_sign and positions[9] == curr_sign:
        return True
    if positions[1] == curr_sign and positions[4] == curr_sign and positions[7] == curr_sign or \
            positions[2] == curr_sign and positions[5] == curr_sign and positions[8] == curr_sign or \
            positions[3] == curr_sign and positions[6] == curr_sign and positions[9] == curr_sign:
        return True
    if positions[1] == curr_sign and positions[5] == curr_sign and positions[9] == curr_sign or \
            positions[3] == curr_sign and positions[5] == curr_sign and positions[7] == curr_sign:
        return True

    return False


player_1_name = input('Player one please write your name: ')
player_2_name = input('Player two please write your name: ')

print(f'Player one name: {player_1_name}')
print(f'Player two name: {player_2_name}')

player_1_sign = input(f"{player_1_name} would you like to play with 'X' or 'O'?")

while player_1_sign != 'X' and player_1_sign != 'O' and player_1_sign != 'x' and player_1_sign != 'o':
    player_1_sign = input(f"{player_1_name} would you like to play with 'X' or 'O'? ")

player_2_sign = 'X' if player_1_sign == 'O' else 'O'

players_data = [[player_1_name, player_1_sign], [player_2_name, player_2_sign]]

print(f'This is the numeration of the board:')
print('| 1 | 2 | 3 |')
print('| 4 | 5 | 6 |')
print('| 7 | 8 | 9 |')

print(f'{player_1_name} starts first!')

win = False
counter = 0
positions = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}

positions_data = {
    1: [0, 0],
    2: [0, 1],
    3: [0, 2],
    4: [1, 0],
    5: [1, 1],
    6: [1, 2],
    7: [2, 0],
    8: [2, 1],
    9: [2, 2]
}

matrix = [[' ' for j in range(3)] for i in range(3)]


curr_player = ''

while not win and counter < 10:
    counter += 1
    curr_player, curr_sign = turn_players(players_data, counter)
    position = 0

    while not is_valid_position(position):
        try:
            position = int(input(f'{curr_player} choose a free position [1-9]: '))
        except ValueError:
            print('You can use only integer numbers.')

    positions[position] = curr_sign.upper()

    win = check_if_wins(positions, curr_sign.upper())

    row, col = positions_data[position]
    matrix[row][col] = curr_sign.upper()

    for r in matrix:
        output = f'| {" | ".join([str(x) for x in r])} |'
        print(output)

if win:
    print(f'{curr_player} wins')
else:
    print('Nobody wins...')
