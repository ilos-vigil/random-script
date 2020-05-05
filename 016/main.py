def print_board(position, board_size):
    # print board
    print('Board!')
    for i in range(board_size):
        text = ''
        for j in range(board_size):
            findQueen = False
            for k in range(board_size):
                if position[k][1] == i and position [k][0] == j:
                    findQueen = True
                    text += 'Q'
                    k = board_size + 1
            if findQueen == False:
                text += '_'
        print(text)

    # print each queen position
    print('Queen position')
    for i in range(board_size):
        print(f'{i}. {position[i][0]},{position[i][1]}')


def eight_queen(x, y, board_size):
    turn = 1
    position = [[0, 0] for i in range(board_size)]
    position[0][0] = x
    position[0][1] = y
    collusion = True

    b = [0 for i in range(board_size)]

    while turn < board_size:
        for i in range(b[turn], board_size):
            position[turn][0] = i
            position[turn][1] = (position[0][1] + turn) % board_size

            collusion = False

            for k in range(turn):
                if position[k][0] == position[turn][0] or position[k][0] - position[k][1] == position[turn][0] - position[turn][1] or position[turn][0] - position[k][0] == position[k][0] - position[turn][0] or position[k][0] + position[k][1] == position[turn][0] + position[turn][1]:
                    collusion = True
                    break

            if collusion == False:
                b[turn] = i + 1
                break

        if collusion == False:
            turn = turn + 1
        else:
            b[turn] = 0
            turn = turn - 1

    print_board(position, board_size)



x = int(input('X: '))
y = int(input('Y: '))
board_size = int(input('Board size: '))
eight_queen(x, y, board_size)
