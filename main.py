import numpy as num

BLACK = '\033[0m'
BLUE = '\033[94m'

board = [["r", "n", "b", "q", "k", "b", "n", "r"],
         ["p", "p", "p", "p", "p", "p", "p", "p"],
         ["_", "_", "_", "_", "_", "_", "_", "_"],
         ["_", "_", "_", "_", "_", "_", "_", "_"],
         ["_", "_", "_", "_", "_", "_", "_", "_"],
         ["_", "_", "_", "_", "_", "_", "_", "_"],
         ["p", "p", "p", "p", "p", "p", "p", "p"],
         ["r", "n", "b", "q", "k", "b", "n", "r"]]

color_board = [[2, 2, 2, 2, 2, 2, 2, 2],
               [2, 2, 2, 2, 2, 2, 2, 2],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [1, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1, 1]]

castle_board = [[1, 0, 0, 0, 1, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 1, 0, 0, 1]]


def remove_en_passant(color):
    for x in range(8):
        for y in range(8):
            if color_board[x][y] == color + 2:
                color_board[x][y] -= 2


def in_check(color):
    try:
        if color[0] == "k":
            if color[3] == "1":
                king_space = [ord(color[1]) - 96, ord(color[2]) - 48]
                color = 1
            else:
                king_space = [ord(color[1]) - 96, ord(color[2]) - 48]
                color = 2
        else:
            king_space = []
            for x in range(8):
                for y in range(8):
                    if board[x][y] == "k" and color_board[x][y] == color:
                        king_space = [y + 1, -1 * (x - 8)]
    except:
        king_space = []
        for x in range(8):
            for y in range(8):
                if board[x][y] == "k" and color_board[x][y] == color:
                    king_space = [y + 1, -1 * (x - 8)]
    for x in range(8):
        for y in range(8):
            if board[x][y] != "_":
                if color_board[x][y] == color - 1 or color_board[x][y] == color + 1 or color_board[x][y] == color + 3:
                    if board[x][y] == "p":
                        moves = pawn_moves("p" + chr(y + 97) + str(-1 * (x - 8)))
                        if moves.count(king_space) > 0:
                            return True
                    if board[x][y] == "r":
                        moves = rook_moves("r" + chr(y + 97) + str(-1 * (x - 8)))
                        if moves.count(king_space) > 0:
                            return True
                    if board[x][y] == "n":
                        moves = knight_moves("n" + chr(y + 97) + str(-1 * (x - 8)))
                        if moves.count(king_space) > 0:
                            return True
                    if board[x][y] == "b":
                        moves = bishop_moves("b" + chr(y + 97) + str(-1 * (x - 8)))
                        if moves.count(king_space) > 0:
                            return True
                    if board[x][y] == "q":
                        moves = queen_moves("q" + chr(y + 97) + str(-1 * (x - 8)))
                        if moves.count(king_space) > 0:
                            return True
    return False


def in_checkmate(color):
    for x in range(8):
        for y in range(8):
            if board[x][y] != "_":
                if color_board[x][y] == color:
                    if board[x][y] == "k":
                        moves = king_moves("k" + chr(y + 97) + str(-1 * (x - 8)))
                        for z in range(len(moves)):
                            taken_piece = board[-1 * (moves[z][1] - 8)][moves[z][0] - 1]
                            taken_color = color_board[-1 * (moves[z][1] - 8)][moves[z][0] - 1]
                            board[x][y] = "_"
                            color_board[x][y] = 0
                            board[-1 * (moves[z][1] - 8)][moves[z][0] - 1] = "k"
                            color_board[-1 * (moves[z][1] - 8)][moves[z][0] - 1] = color
                            if not in_check(color):
                                board[x][y] = "k"
                                color_board[x][y] = color
                                board[-1 * (moves[z][1] - 8)][moves[z][0] - 1] = taken_piece
                                color_board[-1 * (moves[z][1] - 8)][moves[z][0] - 1] = taken_color
                                return False
                            board[x][y] = "k"
                            color_board[x][y] = color
                            board[-1 * (moves[z][1] - 8)][moves[z][0] - 1] = taken_piece
                            color_board[-1 * (moves[z][1] - 8)][moves[z][0] - 1] = taken_color
                    if board[x][y] == "q":
                        moves = queen_moves("q" + chr(y + 97) + str(-1 * (x - 8)))
                        for z in range(len(moves)):
                            taken_piece = board[-1 * (moves[z][1] - 8)][moves[z][0] - 1]
                            taken_color = color_board[-1 * (moves[z][1] - 8)][moves[z][0] - 1]
                            board[x][y] = "_"
                            color_board[x][y] = 0
                            board[-1 * (moves[z][1] - 8)][moves[z][0] - 1] = "q"
                            color_board[-1 * (moves[z][1] - 8)][moves[z][0] - 1] = color
                            if not in_check(color):
                                board[x][y] = "q"
                                color_board[x][y] = color
                                board[-1 * (moves[z][1] - 8)][moves[z][0] - 1] = taken_piece
                                color_board[-1 * (moves[z][1] - 8)][moves[z][0] - 1] = taken_color
                                return False
                            board[x][y] = "q"
                            color_board[x][y] = color
                            board[-1 * (moves[z][1] - 8)][moves[z][0] - 1] = taken_piece
                            color_board[-1 * (moves[z][1] - 8)][moves[z][0] - 1] = taken_color
                    if board[x][y] == "p":
                        moves = pawn_moves("p" + chr(y + 97) + str(-1 * (x - 8)))
                        for z in range(len(moves)):
                            taken_piece = board[-1 * (moves[z][1] - 8)][moves[z][0] - 1]
                            taken_color = color_board[-1 * (moves[z][1] - 8)][moves[z][0] - 1]
                            board[x][y] = "_"
                            color_board[x][y] = 0
                            board[-1 * (moves[z][1] - 8)][moves[z][0] - 1] = "p"
                            color_board[-1 * (moves[z][1] - 8)][moves[z][0] - 1] = color
                            if not in_check(color):
                                board[x][y] = "p"
                                color_board[x][y] = color
                                board[-1 * (moves[z][1] - 8)][moves[z][0] - 1] = taken_piece
                                color_board[-1 * (moves[z][1] - 8)][moves[z][0] - 1] = taken_color
                                return False
                            board[x][y] = "p"
                            color_board[x][y] = color
                            board[-1 * (moves[z][1] - 8)][moves[z][0] - 1] = taken_piece
                            color_board[-1 * (moves[z][1] - 8)][moves[z][0] - 1] = taken_color
                    if board[x][y] == "n":
                        moves = knight_moves("n" + chr(y + 97) + str(-1 * (x - 8)))
                        for z in range(len(moves)):
                            taken_piece = board[-1 * (moves[z][1] - 8)][moves[z][0] - 1]
                            taken_color = color_board[-1 * (moves[z][1] - 8)][moves[z][0] - 1]
                            board[x][y] = "_"
                            color_board[x][y] = 0
                            board[-1 * (moves[z][1] - 8)][moves[z][0] - 1] = "n"
                            color_board[-1 * (moves[z][1] - 8)][moves[z][0] - 1] = color
                            if not in_check(color):
                                board[x][y] = "n"
                                color_board[x][y] = color
                                board[-1 * (moves[z][1] - 8)][moves[z][0] - 1] = taken_piece
                                color_board[-1 * (moves[z][1] - 8)][moves[z][0] - 1] = taken_color
                                return False
                            board[x][y] = "n"
                            color_board[x][y] = color
                            board[-1 * (moves[z][1] - 8)][moves[z][0] - 1] = taken_piece
                            color_board[-1 * (moves[z][1] - 8)][moves[z][0] - 1] = taken_color
                    if board[x][y] == "b":
                        moves = bishop_moves("b" + chr(y + 97) + str(-1 * (x - 8)))
                        for z in range(len(moves)):
                            taken_piece = board[-1 * (moves[z][1] - 8)][moves[z][0] - 1]
                            taken_color = color_board[-1 * (moves[z][1] - 8)][moves[z][0] - 1]
                            board[x][y] = "_"
                            color_board[x][y] = 0
                            board[-1 * (moves[z][1] - 8)][moves[z][0] - 1] = "b"
                            color_board[-1 * (moves[z][1] - 8)][moves[z][0] - 1] = color
                            if not in_check(color):
                                board[x][y] = "b"
                                color_board[x][y] = color
                                board[-1 * (moves[z][1] - 8)][moves[z][0] - 1] = taken_piece
                                color_board[-1 * (moves[z][1] - 8)][moves[z][0] - 1] = taken_color
                                return False
                            board[x][y] = "b"
                            color_board[x][y] = color
                            board[-1 * (moves[z][1] - 8)][moves[z][0] - 1] = taken_piece
                            color_board[-1 * (moves[z][1] - 8)][moves[z][0] - 1] = taken_color
                    if board[x][y] == "r":
                        moves = rook_moves("r" + chr(y + 97) + str(-1 * (x - 8)))
                        for z in range(len(moves)):
                            taken_piece = board[-1 * (moves[z][1] - 8)][moves[z][0] - 1]
                            taken_color = color_board[-1 * (moves[z][1] - 8)][moves[z][0] - 1]
                            board[x][y] = "_"
                            color_board[x][y] = 0
                            board[-1 * (moves[z][1] - 8)][moves[z][0] - 1] = "r"
                            color_board[-1 * (moves[z][1] - 8)][moves[z][0] - 1] = color
                            if not in_check(color):
                                board[x][y] = "r"
                                color_board[x][y] = color
                                board[-1 * (moves[z][1] - 8)][moves[z][0] - 1] = taken_piece
                                color_board[-1 * (moves[z][1] - 8)][moves[z][0] - 1] = taken_color
                                return False
                            board[x][y] = "r"
                            color_board[x][y] = color
                            board[-1 * (moves[z][1] - 8)][moves[z][0] - 1] = taken_piece
                            color_board[-1 * (moves[z][1] - 8)][moves[z][0] - 1] = taken_color
    return True


def print_board_backwards():
    for i in range(8):
        for j in range(8):
            if color_board[-1 * (i - 8) - 1][-1 * (j - 8) - 1] == 2 or \
                    color_board[-1 * (i - 8) - 1][-1 * (j - 8) - 1] == 4:
                print(BLUE + board[-1 * (i - 8) - 1][-1 * (j - 8) - 1] + ' ', end='' + BLACK)
                continue
            print(board[-1 * (i - 8) - 1][-1 * (j - 8) - 1] + ' ', end='')
        print()


def print_board():
    for i in range(8):
        for j in range(8):
            if color_board[i][j] == 2 or color_board[i][j] == 4:
                print(BLUE + board[i][j] + ' ', end='' + BLACK)
                continue
            print(board[i][j] + ' ', end='')
        print()


def make_move(color):
    while True:  # iteration
        try:
            moves = []  # list
            index = input()
            check_en_passant = [" "]
            check_promote = False
            index1os = ord(index[1]) - 96
            index2os = ord(index[2]) - 48
            if index == "O-O-O" and color == 1:  # selection
                if castle_board[7][4] == 1 and castle_board[7][0] == 1 \
                        and not in_check("kd11") \
                        and not in_check("kc11") \
                        and board[7][3] == "_" \
                        and board[7][2] == "_" \
                        and board[7][1] == "_":
                    board[7][4] = "_"
                    board[7][0] = "_"
                    castle_board[7][4] = 0
                    castle_board[7][0] = 0
                    board[7][2] = "k"
                    board[7][3] = "r"
                    color_board[7][4] = 0
                    color_board[7][0] = 0
                    color_board[7][2] = 1
                    color_board[7][3] = 1
                    break
                else:
                    print("move not viable")
                    continue
            if index == "O-O" and color == 1:
                if castle_board[7][4] == 1 and castle_board[7][7] == 1 \
                        and not in_check("kf11") \
                        and not in_check("kg11") \
                        and board[7][5] == "_" \
                        and board[7][6] == "_":
                    board[7][4] = "_"
                    board[7][7] = "_"
                    castle_board[7][4] = 0
                    castle_board[7][7] = 0
                    board[7][6] = "k"
                    board[7][5] = "r"
                    color_board[7][4] = 0
                    color_board[7][7] = 0
                    color_board[7][6] = 1
                    color_board[7][5] = 1
                    break
                else:
                    print("move not viable")
                    continue
            if index == "O-O-O" and color == 2:
                if castle_board[0][4] == 1 and castle_board[0][0] == 1 \
                        and not in_check("kd82") \
                        and not in_check("kc82") \
                        and board[0][3] == "_" \
                        and board[0][2] == "_" \
                        and board[0][1] == "_":
                    board[0][4] = "_"
                    board[0][0] = "_"
                    castle_board[0][4] = 0
                    castle_board[0][7] = 0
                    board[0][2] = "k"
                    board[0][3] = "r"
                    color_board[0][4] = 0
                    color_board[0][0] = 0
                    color_board[0][2] = 2
                    color_board[0][3] = 2
                    break
                else:
                    print("move not viable")
                    continue
            if index == "O-O" and color == 2:
                if castle_board[0][4] == 1 and castle_board[0][7] == 1 \
                        and not in_check("kf82") \
                        and not in_check("kg82") \
                        and board[0][5] == "_" \
                        and board[0][6] == "_":
                    board[0][4] = "_"
                    board[0][7] = "_"
                    castle_board[0][4] = 0
                    castle_board[0][7] = 0
                    board[0][6] = "k"
                    board[0][5] = "r"
                    color_board[0][4] = 0
                    color_board[0][7] = 0
                    color_board[0][6] = 2
                    color_board[0][5] = 2
                    break
                else:
                    print("move not viable")
                    continue
            if len(index) == 7:
                index1ms = ord(index[5]) - 96
                index2ms = ord(index[6]) - 48
                check_promote = True
            else:
                index1ms = ord(index[4]) - 96
                index2ms = ord(index[5]) - 48
            if index[0] == "p" and (index2ms == 8 or index2ms == 1) and \
                    index[4] != "q" and index[4] != "r" and index[4] != "b" and index[4] != "n":
                print("move not viable")
                continue
            index1os -= 1
            index2os -= 1
            index1ms -= 1
            index2ms -= 1
            move_space = [index1ms + 1, index2ms + 1]
            if find_color(index) == color:
                if index[0] == "p" and board[-1 * (index2os - 8) - 1][index1os] == "p":
                    moves = pawn_moves(index)
                if index[0] == "n" and board[-1 * (index2os - 8) - 1][index1os] == "n":
                    moves = knight_moves(index)
                if index[0] == "b" and board[-1 * (index2os - 8) - 1][index1os] == "b":
                    moves = bishop_moves(index)
                if index[0] == "r" and board[-1 * (index2os - 8) - 1][index1os] == "r":
                    moves = rook_moves(index)
                if index[0] == "q" and board[-1 * (index2os - 8) - 1][index1os] == "q":
                    moves = queen_moves(index)
                if index[0] == "k" and board[-1 * (index2os - 8) - 1][index1os] == "k":
                    moves = king_moves(index)
            if moves.count(move_space) > 0:
                board[-1 * (index2os - 8) - 1][index1os] = "_"
                board[-1 * (index2ms - 8) - 1][index1ms] = str(index[0])
                color_board[-1 * (index2os - 8) - 1][index1os] = 0
                color_board[-1 * (index2ms - 8) - 1][index1ms] = color
                if in_check(color):
                    board[-1 * (index2os - 8) - 1][index1os] = str(index[0])
                    board[-1 * (index2ms - 8) - 1][index1ms] = "_"
                    color_board[-1 * (index2os - 8) - 1][index1os] = color
                    color_board[-1 * (index2ms - 8) - 1][index1ms] = 0
                    print("move not viable")
                    continue
                if index[0] == "p":
                    if index2os - index2ms == 2 or index2os - index2ms == -2:
                        color_board[-1 * (index2ms - 8) - 1][index1ms] = color + 2
                        break
                    check_en_passant.append(chr(index1ms + 97))
                    check_en_passant.append(str(index2ms))
                    if color == 1 and find_color(check_en_passant) == 4:
                        color_board[-1 * (index2ms - 8)][index1ms] = 0
                        board[-1 * (index2ms - 8)][index1ms] = "_"
                        if in_check(color):
                            board[-1 * (index2os - 8) - 1][index1os] = str(index[0])
                            board[-1 * (index2ms - 8) - 1][index1ms] = "_"
                            color_board[-1 * (index2os - 8) - 1][index1os] = color
                            color_board[-1 * (index2ms - 8) - 1][index1ms] = 0
                            color_board[-1 * (index2ms - 8) - 2][index1ms] = 4
                            board[-1 * (index2ms - 8) - 2][index1ms] = "p"
                            print("move not viable")
                            continue
                        break
                    check_en_passant = [" "]
                    check_en_passant.append(chr(index1ms + 97))
                    check_en_passant.append(str(index2ms + 2))
                    if color == 2 and find_color(check_en_passant) == 3:
                        color_board[-1 * (index2ms - 8) - 2][index1ms] = 0
                        board[-1 * (index2ms - 8) - 2][index1ms] = "_"
                        if in_check(color):
                            board[-1 * (index2os - 8) - 1][index1os] = str(index[0])
                            board[-1 * (index2ms - 8) - 1][index1ms] = "_"
                            color_board[-1 * (index2os - 8) - 1][index1os] = color
                            color_board[-1 * (index2ms - 8) - 1][index1ms] = 0
                            color_board[-1 * (index2ms - 8) - 2][index1ms] = 3
                            board[-1 * (index2ms - 8) - 2][index1ms] = "p"
                            print("move not viable")
                            continue
                        break
                    if check_promote:
                        color_board[-1 * (index2ms - 8) - 1][index1ms] = color
                        board[-1 * (index2ms - 8) - 1][index1ms] = index[4]
                        if in_check(color):
                            board[-1 * (index2os - 8) - 1][index1os] = str(index[0])
                            board[-1 * (index2ms - 8) - 1][index1ms] = "_"
                            color_board[-1 * (index2os - 8) - 1][index1os] = color
                            color_board[-1 * (index2ms - 8) - 1][index1ms] = 0
                            print("move not viable")
                            continue
                if index[0] == "r" or index[0] == "k":
                    castle_board[-1 * (index2os - 8) - 1][index1os] = 0
                break
            else:
                print("move not viable")
        except:

            print("move not viable")


def find_color(index):
    index1 = ord(index[1]) - 97
    index2 = ord(index[2]) - 48
    return color_board[-1 * (index2 - 8)][index1]


def knight_moves(index):
    string_list = [" "]
    index1 = ord(index[1]) - 96
    index2 = ord(index[2]) - 48
    mylist = []
    board_index1 = -1 * (index2 - 8)
    board_index2 = index1 - 1
    string_list.append(chr(index1 + 96))
    string_list.append(str(index2))
    color = find_color(string_list)
    # knight going up and right
    if board_index1 - 2 >= 0 and board_index2 + 1 < 8 and index1 + 1 <= 8 and index2 + 2 <= 8:
        if color_board[board_index1 - 2][board_index2 + 1] != color and color_board[board_index1 - 2][board_index2 + 1] != color + 2:
            mylist.append([index1 + 1, index2 + 2])
    if board_index1 - 1 >= 0 and board_index2 + 2 < 8 and index1 + 2 <= 8 and index2 + 1 <= 8:
        if color_board[board_index1 - 1][board_index2 + 2] != color and color_board[board_index1 - 1][board_index2 + 2] != color + 2:
            mylist.append([index1 + 2, index2 + 1])
    # knight going down and right
    if board_index1 + 1 < 8 and board_index2 + 2 < 8 and index1 + 2 <= 8 and index2 - 1 > 0:
        if color_board[board_index1 + 1][board_index2 + 2] != color and color_board[board_index1 + 1][board_index2 + 2] != color + 2:
            mylist.append([index1 + 2, index2 - 1])
    if board_index1 + 2 < 8 and board_index2 + 1 < 8 and index1 + 1 <= 8 and index2 - 2 > 0:
        if color_board[board_index1 + 2][board_index2 + 1] != color and color_board[board_index1 + 2][board_index2 + 1] != color + 2:
            mylist.append([index1 + 1, index2 - 2])
    # knight going down and left
    if board_index1 + 2 < 8 and board_index2 - 1 >= 0 and index1 - 1 > 0 and index2 - 2 > 0:
        if color_board[board_index1 + 2][board_index2 - 1] != color and color_board[board_index1 + 2][board_index2 - 1] != color + 2:
            mylist.append([index1 - 1, index2 - 2])
    if board_index1 + 1 < 8 and board_index2 - 2 >= 0 and index1 - 2 > 0 and index2 - 1 > 0:
        if color_board[board_index1 + 1][board_index2 - 2] != color and color_board[board_index1 + 1][board_index2 - 2] != color + 2:
            mylist.append([index1 - 2, index2 - 1])
    # knight going up and left
    if board_index1 - 1 >= 0 and board_index2 - 2 >= 0 and index1 - 2 > 0 and index2 + 1 <= 8:
        if color_board[board_index1 - 1][board_index2 - 2] != color and color_board[board_index1 - 1][board_index2 - 2] != color + 2:
            mylist.append([index1 - 2, index2 + 1])
    if board_index1 - 2 >= 0 and board_index2 - 1 >= 0 and index1 - 1 > 0 and index2 + 2 <= 8:
        if color_board[board_index1 - 2][board_index2 - 1] != color and color_board[board_index1 - 2][board_index2 - 1] != color + 2:
            mylist.append([index1 - 1, index2 + 2])
    return mylist


def bishop_moves(index):
    string_list = [" "]
    index1 = ord(index[1]) - 96
    index2 = ord(index[2]) - 48
    list = []
    index1 -= 1
    index2 -= 1
    control1 = index1
    control2 = index2
    # up and right
    while 0 <= index1 < 8 and 0 <= index2 < 8:
        if (index1, index2) == (control1, control2):
            index1 += 1
            index2 += 1
            continue
        if board[-1 * (index2 - 8) - 1][index1] != "_":
            string_list.append(chr(index1 + 97))
            string_list.append(str(index2 + 1))
            if find_color(index) != find_color(string_list):
                list.append([index1, index2])
                break
            else:
                break
        list.append([index1, index2])
        index1 += 1
        index2 += 1
    index1 = control1
    index2 = control2
    string_list = [" "]
    # down and left
    while 0 <= index1 < 8 and 0 <= index2 < 8:
        if (index1, index2) == (control1, control2):
            index1 -= 1
            index2 -= 1
            continue
        if board[-1 * (index2 - 8) - 1][index1] != "_":
            string_list.append(chr(index1 + 97))
            string_list.append(str(index2 + 1))
            if find_color(index) != find_color(string_list):
                list.append([index1, index2])
                break
            else:
                break
        list.append([index1, index2])
        index1 -= 1
        index2 -= 1
    index1 = control1
    index2 = control2
    string_list = [" "]
    # up and left
    while 0 <= index1 < 8 and 0 <= index2 < 8:
        if (index1, index2) == (control1, control2):
            index1 -= 1
            index2 += 1
            continue
        if board[-1 * (index2 - 8) - 1][index1] != "_":
            string_list.append(chr(index1 + 97))
            string_list.append(str(index2 + 1))
            if find_color(index) != find_color(string_list):
                list.append([index1, index2])
                break
            else:
                break
        list.append([index1, index2])
        index1 -= 1
        index2 += 1
    index1 = control1
    index2 = control2
    string_list = [" "]
    # down and right
    while 0 <= index1 < 8 and 0 <= index2 < 8:
        if (index1, index2) == (control1, control2):
            index1 += 1
            index2 -= 1
            continue
        if board[-1 * (index2 - 8) - 1][index1] != "_":
            string_list.append(chr(index1 + 97))
            string_list.append(str(index2 + 1))
            if find_color(index) != find_color(string_list):
                list.append([index1, index2])
                break
            else:
                break
        list.append([index1, index2])
        index1 += 1
        index2 -= 1
    mylist = num.array(list)
    mylist += 1
    return_list = mylist.tolist()
    return return_list


def rook_moves(index):
    string_list = [" "]
    index1 = ord(index[1]) - 96
    index2 = ord(index[2]) - 48
    list = []
    index1 -= 1
    index2 -= 1
    control1 = index1
    control2 = index2
    # right
    while 0 <= index1 < 8 and 0 <= index2 < 8:
        if (index1, index2) == (control1, control2):
            index1 += 1
            continue
        if board[-1 * (index2 - 8) - 1][index1] != "_":
            string_list.append(chr(index1 + 97))
            string_list.append(str(index2 + 1))
            if find_color(index) != find_color(string_list):
                list.append([index1, index2])
                break
            else:
                break
        list.append([index1, index2])
        index1 += 1
    index1 = control1
    index2 = control2
    string_list = [" "]
    # left
    while 0 <= index1 < 8 and 0 <= index2 < 8:
        if (index1, index2) == (control1, control2):
            index1 -= 1
            continue
        if board[-1 * (index2 - 8) - 1][index1] != "_":
            string_list.append(chr(index1 + 97))
            string_list.append(str(index2 + 1))
            if find_color(index) != find_color(string_list):
                list.append([index1, index2])
                break
            else:
                break
        list.append([index1, index2])
        index1 -= 1
    index1 = control1
    index2 = control2
    string_list = [" "]
    # up
    while 0 <= index1 < 8 and 0 <= index2 < 8:
        if (index1, index2) == (control1, control2):
            index2 += 1
            continue
        if board[-1 * (index2 - 8) - 1][index1] != "_":
            string_list.append(chr(index1 + 97))
            string_list.append(str(index2 + 1))
            if find_color(index) != find_color(string_list):
                list.append([index1, index2])
                break
            else:
                break
        list.append([index1, index2])
        index2 += 1
    index1 = control1
    index2 = control2
    string_list = [" "]
    # down
    while 0 <= index1 < 8 and 0 <= index2 < 8:
        if (index1, index2) == (control1, control2):
            index2 -= 1
            continue
        if board[-1 * (index2 - 8) - 1][index1] != "_":
            string_list.append(chr(index1 + 97))
            string_list.append(str(index2 + 1))
            if find_color(index) != find_color(string_list):
                list.append([index1, index2])
                break
            else:
                break
        list.append([index1, index2])
        index2 -= 1
    mylist = num.array(list)
    mylist += 1
    return_list = mylist.tolist()
    return return_list


def queen_moves(index):
    string_list = [" "]
    index1 = ord(index[1]) - 96
    index2 = ord(index[2]) - 48
    list = []
    index1 -= 1
    index2 -= 1
    control1 = index1
    control2 = index2
    # up and right
    while 0 <= index1 < 8 and 0 <= index2 < 8:
        if (index1, index2) == (control1, control2):
            index1 += 1
            index2 += 1
            continue
        if board[-1 * (index2 - 8) - 1][index1] != "_":
            string_list.append(chr(index1 + 97))
            string_list.append(str(index2 + 1))
            if find_color(index) != find_color(string_list):
                list.append([index1, index2])
                break
            else:
                break
        list.append([index1, index2])
        index1 += 1
        index2 += 1
    index1 = control1
    index2 = control2
    string_list = [" "]
    # down and left
    while 0 <= index1 < 8 and 0 <= index2 < 8:
        if (index1, index2) == (control1, control2):
            index1 -= 1
            index2 -= 1
            continue
        if board[-1 * (index2 - 8) - 1][index1] != "_":
            string_list.append(chr(index1 + 97))
            string_list.append(str(index2 + 1))
            if find_color(index) != find_color(string_list):
                list.append([index1, index2])
                break
            else:
                break
        list.append([index1, index2])
        index1 -= 1
        index2 -= 1
    index1 = control1
    index2 = control2
    string_list = [" "]
    # up and left
    while 0 <= index1 < 8 and 0 <= index2 < 8:
        if (index1, index2) == (control1, control2):
            index1 -= 1
            index2 += 1
            continue
        if board[-1 * (index2 - 8) - 1][index1] != "_":
            string_list.append(chr(index1 + 97))
            string_list.append(str(index2 + 1))
            if find_color(index) != find_color(string_list):
                list.append([index1, index2])
                break
            else:
                break
        list.append([index1, index2])
        index1 -= 1
        index2 += 1
    index1 = control1
    index2 = control2
    string_list = [" "]
    # down and right
    while 0 <= index1 < 8 and 0 <= index2 < 8:
        if (index1, index2) == (control1, control2):
            index1 += 1
            index2 -= 1
            continue
        if board[-1 * (index2 - 8) - 1][index1] != "_":
            string_list.append(chr(index1 + 97))
            string_list.append(str(index2 + 1))
            if find_color(index) != find_color(string_list):
                list.append([index1, index2])
                break
            else:
                break
        list.append([index1, index2])
        index1 += 1
        index2 -= 1
    index1 = control1
    index2 = control2
    string_list = [" "]
    # right
    while 0 <= index1 < 8 and 0 <= index2 < 8:
        if (index1, index2) == (control1, control2):
            index1 += 1
            continue
        if board[-1 * (index2 - 8) - 1][index1] != "_":
            string_list.append(chr(index1 + 97))
            string_list.append(str(index2 + 1))
            if find_color(index) != find_color(string_list):
                list.append([index1, index2])
                break
            else:
                break
        list.append([index1, index2])
        index1 += 1
    index1 = control1
    index2 = control2
    string_list = [" "]
    # left
    while 0 <= index1 < 8 and 0 <= index2 < 8:
        if (index1, index2) == (control1, control2):
            index1 -= 1
            continue
        if board[-1 * (index2 - 8) - 1][index1] != "_":
            string_list.append(chr(index1 + 97))
            string_list.append(str(index2 + 1))
            if find_color(index) != find_color(string_list):
                list.append([index1, index2])
                break
            else:
                break
        list.append([index1, index2])
        index1 -= 1
    index1 = control1
    index2 = control2
    string_list = [" "]
    # up
    while 0 <= index1 < 8 and 0 <= index2 < 8:
        if (index1, index2) == (control1, control2):
            index2 += 1
            continue
        if board[-1 * (index2 - 8) - 1][index1] != "_":
            string_list.append(chr(index1 + 97))
            string_list.append(str(index2 + 1))
            if find_color(index) != find_color(string_list):
                list.append([index1, index2])
                break
            else:
                break
        list.append([index1, index2])
        index2 += 1
    index1 = control1
    index2 = control2
    string_list = [" "]
    # down
    while 0 <= index1 < 8 and 0 <= index2 < 8:
        if (index1, index2) == (control1, control2):
            index2 -= 1
            continue
        if board[-1 * (index2 - 8) - 1][index1] != "_":
            string_list.append(chr(index1 + 97))
            string_list.append(str(index2 + 1))
            if find_color(index) != find_color(string_list):
                list.append([index1, index2])
                break
            else:
                break
        list.append([index1, index2])
        index2 -= 1
    mylist = num.array(list)
    mylist += 1
    return_list = mylist.tolist()
    return return_list


def king_moves(index):
    string_list = [" "]
    index1 = ord(index[1]) - 96
    index2 = ord(index[2]) - 48
    mylist = []
    board_index1 = -1 * (index2 - 8)
    board_index2 = index1 - 1
    string_list.append(chr(index1 + 96))
    string_list.append(str(index2))
    color = find_color(string_list)
    if index2 + 1 <= 8:
        if color_board[board_index1 - 1][board_index2] != color and color_board[board_index1 - 1][board_index2] != color + 2:
            mylist.append([index1, index2 + 1])
    if index1 + 1 <= 8 and index2 + 1 <= 8:
        if color_board[board_index1 - 1][board_index2 + 1] != color and color_board[board_index1 - 1][board_index2 + 1] != color + 2:
            mylist.append([index1 + 1, index2 + 1])
    if index1 + 1 <= 8:
        if color_board[board_index1][board_index2 + 1] != color and color_board[board_index1][board_index2 + 1] != color + 2:
            mylist.append([index1 + 1, index2])
    if index1 + 1 <= 8 and index2 - 1 > 0:
        if color_board[board_index1 + 1][board_index2 + 1] != color and color_board[board_index1 + 1][board_index2 + 1] != color + 2:
            mylist.append([index1 + 1, index2 - 1])
    if index2 - 1 > 0:
        if color_board[board_index1 + 1][board_index2] != color and color_board[board_index1 + 1][board_index2] != color + 2:
            mylist.append([index1, index2 - 1])
    if index1 - 1 > 0 and index2 - 1 > 0:
        if color_board[board_index1 + 1][board_index2 - 1] != color and color_board[board_index1 + 1][board_index2 - 1] != color + 2:
            mylist.append([index1 - 1, index2 - 1])
    if index1 - 1 > 0:
        if color_board[board_index1][board_index2 - 1] != color and color_board[board_index1][board_index2 - 1] != color + 2:
            mylist.append([index1 - 1, index2])
    if index1 - 1 > 0 and index2 + 1 <= 8:
        if color_board[board_index1 - 1][board_index2 - 1] != color and color_board[board_index1 - 1][board_index2 - 1] != color + 2:
            mylist.append([index1 - 1, index2 + 1])
    return mylist


def pawn_moves(index):
    color_find_list = [" "]
    mylist = []
    color = find_color(index)
    index1 = ord(index[1]) - 96
    index2 = ord(index[2]) - 48
    index1 -= 1
    index2 -= 1
    if color == 1:
        color_find_list.append(chr(index1 + 96))
        color_find_list.append(str(index2 + 2))
        try:
            if (find_color(color_find_list) == color + 1
                or find_color(color_find_list) == color + 3) \
                    and (0 <= -1 * (index2 - 8) - 2 <= 8 and 0 <= index1 - 1 <= 8):
                mylist.append([index1, index2 + 2])
            color_find_list = [" "]
        except:
            color_find_list = [" "]
        try:
            color_find_list.append(chr(index1 + 98))
            color_find_list.append(str(index2 + 2))
            if (find_color(color_find_list) == color + 1
                or find_color(color_find_list) == color + 3) \
                    and (0 <= -1 * (index2 - 8) - 2 <= 8 and 0 <= index1 + 1 <= 8):
                mylist.append([index1 + 2, index2 + 2])
            color_find_list = [" "]
        except:
            color_find_list = [" "]
        if index2 == 1 and board[(-1 * (index2 - 8) - 3)][index1] == "_" \
                and board[(-1 * (index2 - 8) - 2)][index1] == "_":
            mylist.append([index1 + 1, index2 + 2])
            mylist.append([index1 + 1, index2 + 3])
        elif index2 < 7 and board[(-1 * (index2 - 8) - 2)][index1] == "_":
            mylist.append([index1 + 1, index2 + 2])
        color_find_list.append(chr(index1 + 96))
        color_find_list.append(str(index2 + 1))
        if index2 == 4:
            try:
                if find_color(color_find_list) == 4:
                    mylist.append([index1, index2 + 2])
            except:
                print()
            color_find_list = [" "]
            color_find_list.append(chr(index1 + 98))
            color_find_list.append(str(index2 + 1))
            try:
                if find_color(color_find_list) == 4:
                    mylist.append([index1 + 2, index2 + 2])
            except:
                print()
    if color == 2:
        color_find_list.append(chr(index1 + 96))
        color_find_list.append(str(index2))
        try:
            if (find_color(color_find_list) == color - 1
                or find_color(color_find_list) == color + 1) \
                    and (0 <= -1 * (index2 - 8) - 2 <= 8 and 0 <= index1 - 1 <= 8):
                mylist.append([index1, index2])
            color_find_list = [" "]
        except:
            color_find_list = [" "]
        try:
            color_find_list.append(chr(index1 + 98))
            color_find_list.append(str(index2))
            if (find_color(color_find_list) == color - 1
                or find_color(color_find_list) == color + 1) \
                    and (0 <= -1 * (index2 - 8) - 2 <= 8 and 0 <= index1 + 1 <= 8):
                mylist.append([index1 + 2, index2])
            color_find_list = [" "]
        except:
            color_find_list = [" "]
        if index2 == 6 and board[(-1 * (index2 - 8) + 1)][index1] == "_" \
                and board[(-1 * (index2 - 8))][index1] == "_":
            mylist.append([index1 + 1, index2 - 1])
            mylist.append([index1 + 1, index2])
        elif index2 > 0 and board[(-1 * (index2 - 8))][index1] == "_":
            mylist.append([index1 + 1, index2])
        color_find_list.append(chr(index1 + 96))
        color_find_list.append(str(index2 + 1))
        if index2 == 3:
            try:
                if find_color(color_find_list) == 3:
                    mylist.append([index1, index2])
            except:
                print()
            color_find_list = [" "]
            color_find_list.append(chr(index1 + 98))
            color_find_list.append(str(index2 + 1))
            try:
                if find_color(color_find_list) == 3:
                    mylist.append([index1 + 2, index2])
            except:
                print()
    return mylist


print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("To move, first type the letter you want to move and the square it is on.")
print("Then, put a space and the square you want to move the piece to. (e.g. pe2 e4)")
print("To short castle, input O-O, and to long castle, type O-O-O")
print("\n\n")
while True:
    print_board()
    if in_checkmate(1):
        print("white is in checkmate")
        break
    else:
        make_move(1)
        while in_check(1):
            print("move not viable")
            make_move(1)
    remove_en_passant(2)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print_board_backwards()
    if in_checkmate(2):
        print("black is in checkmate")
        break
    else:
        make_move(2)
        while in_check(2):
            print("move not viable")
            make_move(2)
    remove_en_passant(1)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
