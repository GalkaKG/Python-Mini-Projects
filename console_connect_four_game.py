from colorama import Fore, Back


def choose_a_player(players_turn, counter):
    if counter % 2 == 0:
        player = players_turn[1][0]
        player_sign = players_turn[1][1]
    else:
        player = players_turn[0][0]
        player_sign = players_turn[0][1]
    return player, player_sign


def is_valid(curr_row, curr_col):
    if 0 <= curr_row < 6 and 0 <= curr_col < 7:
        return True


def tracking_connected(board, curr_row, curr_col, player, player_sign, connected_dict):
    neighbours = [
        (-1, 0),
        (+1, 0),
        (0, -1),
        (0, +1),
        (-1, -1),
        (-1, +1),
        (+1, -1),
        (+1, +1)
    ]

    row, col = curr_row, curr_col

    for r, c in neighbours:
        while is_valid(curr_row, curr_col) and board[curr_row][curr_col] == player_sign:
            connected_dict[player] += 1
            curr_row, curr_col = curr_row + r, curr_col + c
        if connected_dict[player] == 4:
            return player, not win
        else:
            connected_dict[player] = 0

        curr_row, curr_col = row, col

    return player, win


board = [[0] * 7 for _ in range(6)]

players_turn = [['Player 1', 1], ['Player 2', 2]]
counter = 0
win = False
row = 5

player = ''
connected_dict = {'Player 1': 0, 'Player 2': 0}

while not win:
    counter += 1
    player, player_sign = choose_a_player(players_turn, counter)
    print(Back.CYAN + Fore.BLACK + f'{player}, please choose a column: ')
    col = int(input()) - 1

    if is_valid(0, col) and board[0][col] != 0:
        print('This column is full. Please choose another one.')
        print()
        continue

    curr_row = row

    try:
        if board[row][col] == 0:
            board[row][col] = player_sign
        else:
            for idx_row in range(5, -1, -1):
                if board[idx_row][col] == 0:
                    board[idx_row][col] = player_sign
                    curr_row = idx_row
                    break

    except IndexError:
        if col < 0 or col >= 6:
            print('Please choose a number between 1 and 7')
            print()
            continue

    [print(Back.CYAN + Fore.BLACK + f'{row}') for row in board]
    print()
    player, win = tracking_connected(board, curr_row, col, player, player_sign, connected_dict)

print(f'The winner is {player}')
