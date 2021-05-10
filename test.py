import main
import ai

def convert_board(size, board):
    board = board.replace('\n', '')
    board = board.replace(' ', '')
    board = [board[i:i + size] for i in range(0, len(board), size)]
    # Check that the board is valid
    for i, line in enumerate(board):
        for j, c in enumerate(line):
            if (i + j) % 2 == 0 and c != '_':
                raise Exception("Invalid board: expected '_' at row {}, column {}".format(i, j))
    return board

def uniform_moves(moves):
    return [[list(m) for m in mm] for mm in moves]

def check_moves(moves, ground_truth):
    moves = uniform_moves(moves)
    ground_truth = uniform_moves(ground_truth)
    ok = True
    for move in moves:
        if move not in ground_truth:
            print("FAILED: unexpected move: " + str(move))
            ok = False
    for move in ground_truth:
        if move not in moves:
            print("FAILED: missing move: " + str(move))
            ok = False
    if ok:
        print("OK")
    return ok

def test_01_move_black_disc():
    board = convert_board(8, """
________
________
________
__b_____
________
________
_____w__
________
""")
    ground_truth = [[(3, 2), (4, 1)],
                    [(3, 2), (4, 3)]]
    moves = ai.allowed_moves(board, 'b')
    return board, ground_truth, check_moves(moves, ground_truth)

def test_02_move_black_disc_border():
    board = convert_board(8, """
________
________
________
b_______
________
________
_____w__
________
""")
    ground_truth = [[(3, 0), (4, 1)]]
    moves = ai.allowed_moves(board, 'b')
    return board, ground_truth, check_moves(moves, ground_truth)

def test_03_move_white_disc():
    board = convert_board(8, """
________
________
________
__b_____
________
________
_____w__
________
""")
    ground_truth = [[(6, 5), (5, 6)],
                    [(6, 5), (5, 4)]]
    moves = ai.allowed_moves(board, 'w')
    return board, ground_truth, check_moves(moves, ground_truth)

def test_04_move_black_king():
    board = convert_board(8, """
________
________
________
__B_____
________
________
_____w__
________
""")
    ground_truth = [[(3, 2), (4, 1)],
                    [(3, 2), (4, 3)],
                    [(3, 2), (2, 1)],
                    [(3, 2), (2, 3)]]
    moves = ai.allowed_moves(board, 'b')
    return board, ground_truth, check_moves(moves, ground_truth)

def test_05_move_black_king():
    board = convert_board(8, """
________
________
________
__B_____
________
________
_____W__
________
""")
    ground_truth = [[(6, 5), (5, 6)],
                    [(6, 5), (5, 4)],
                    [(6, 5), (7, 6)],
                    [(6, 5), (7, 4)]]
    moves = ai.allowed_moves(board, 'w')
    return board, ground_truth, check_moves(moves, ground_truth)

def test_06_move_black_initial():
    board = convert_board(8, """
_b_b_b_b
b_b_b_b_
_b_b_b_b
________
________
w_w_w_w_
_w_w_w_w
w_w_w_w_
""")
    ground_truth = [[(2, 1), (3, 0)],
                    [(2, 1), (3, 2)],
                    [(2, 3), (3, 2)],
                    [(2, 3), (3, 4)],
                    [(2, 5), (3, 4)],
                    [(2, 5), (3, 6)],
                    [(2, 7), (3, 6)]]
    moves = ai.allowed_moves(board, 'b')
    return board, ground_truth, check_moves(moves, ground_truth)

def test_07_move_white_initial():
    board = convert_board(8, """
_b_b_b_b
b_b_b_b_
_b_b_b_b
________
________
w_w_w_w_
_w_w_w_w
w_w_w_w_
""")
    ground_truth = [[(5, 6), (4, 7)],
                    [(5, 6), (4, 5)],
                    [(5, 4), (4, 5)],
                    [(5, 4), (4, 3)],
                    [(5, 2), (4, 3)],
                    [(5, 2), (4, 1)],
                    [(5, 0), (4, 1)]]
    moves = ai.allowed_moves(board, 'w')
    return board, ground_truth, check_moves(moves, ground_truth)

def test_08_capture_black_simple():
    board = convert_board(8, """
________
________
________
__b_____
___w____
________
________
________
""")
    ground_truth = [[(3, 2), (5, 4)]]
    moves = ai.allowed_moves(board, 'b')
    return board, ground_truth, check_moves(moves, ground_truth)

def test_09_capture_white_simple():
    board = convert_board(8, """
________
__w_____
________
________
________
________
___b_b__
____w___
""")
    ground_truth = [[(7, 4), (5, 6)], [(7, 4), (5, 2)]]
    moves = ai.allowed_moves(board, 'w')
    return board, ground_truth, check_moves(moves, ground_truth)

def test_10_capture_black_multiple():
    board = convert_board(8, """
_____b__
____w___
________
__w___b_
________
__W_____
________
________
""")
    ground_truth = [[(0, 5), (2, 3), (4, 1), (6, 3)]]
    moves = ai.allowed_moves(board, 'b')
    return board, ground_truth, check_moves(moves, ground_truth)

def test_11_capture_white_king():
    board = convert_board(8, """
_____W__
____b_b_
________
__B___w_
________
__b_____
________
________
""")
    ground_truth = [[(0, 5), (2, 7)], [(0, 5), (2, 3), (4, 1), (6, 3)]]
    moves = ai.allowed_moves(board, 'w')
    return board, ground_truth, check_moves(moves, ground_truth)

def test_12_english_rules_no_backward():
    board = convert_board(8, """
________
________
___b_b__
__w_____
________
________
________
________
""")
    ground_truth = [[(3, 2), (1, 4)]]
    moves = ai.allowed_moves(board, 'w')
    return board, ground_truth, check_moves(moves, ground_truth)

def test_13_english_rules_no_long_jump():
    board = convert_board(8, """
_____W__
________
___b____
________
________
________
________
________
""")
    ground_truth = [[(0, 5), (1, 4)],
                    [(0, 5), (1, 6)]]
    moves = ai.allowed_moves(board, 'w')
    return board, ground_truth, check_moves(moves, ground_truth)

def test_14_capture_white_king_in_middle():
    board = convert_board(8, """
________
____b_b_
___w____
________
________
________
________
________
""")
    ground_truth = [[(2, 3), (0, 5), (2, 7)]]
    moves = ai.allowed_moves(board, 'w')
    return board, ground_truth, check_moves(moves, ground_truth)

def test_15_capture_combo():
    board = convert_board(8, """
________
b___b___
_w_w_w__
________
_w_w_W__
________
_W_w____
____B___
""")
    ground_truth = [
        [(1, 0), (3, 2), (5, 0), (7, 2), (5, 4), (3, 2)],
        [(1, 0), (3, 2), (5, 0), (7, 2), (5, 4), (3, 6)],
        [(1, 0), (3, 2), (5, 4), (7, 2), (5, 0), (3, 2)],
        [(1, 4), (3, 2), (5, 0), (7, 2), (5, 4), (3, 2)],
        [(1, 4), (3, 2), (5, 4), (7, 2), (5, 0), (3, 2)],
        [(1, 4), (3, 2), (5, 0), (7, 2), (5, 4), (3, 6), (1, 4)],
        [(1, 4), (3, 6), (5, 4), (7, 2), (5, 0), (3, 2), (5, 4)],
        [(1, 4), (3, 6), (5, 4), (7, 2), (5, 0), (3, 2), (1, 4)],
        [(7, 4), (5, 2), (7, 0)],
        [(7, 4), (5, 2), (3, 0), (1, 2), (3, 4), (5, 2), (7, 0)],
        [(7, 4), (5, 2), (3, 0), (1, 2), (3, 4), (5, 6)],
        [(7, 4), (5, 2), (3, 0), (1, 2), (3, 4), (1, 6)],
        [(7, 4), (5, 2), (3, 4), (5, 6)],
        [(7, 4), (5, 2), (3, 4), (1, 2), (3, 0), (5, 2), (7, 0)],
        [(7, 4), (5, 2), (3, 4), (1, 6)]
    ]
    moves = ai.allowed_moves(board, 'b')
    return board, ground_truth, check_moves(moves, ground_truth)


###############################################################################

if __name__ == "__main__":
    def check_valid_position(test_name, board):
        for row, line in enumerate(board):
            for col, square in enumerate(line):
                if (row + col) % 2 == 0:
                    if square != '_':
                        raise Exception("Ground truth for %s at row %d and column %d (starting at 0) is not valid, it should be '_' as it is a white square." % (test_name, row, col))
    for test_name in dir():
        if test_name.startswith("test_"):
            print("Running '%s':" % test_name)
            (board, ground_truth, ok) = eval("%s()" % test_name)
            check_valid_position(test_name, board)
            if not ok:
                main.print_board(board)
                break
    if ok:
        print("You are good to go ! You can try your script against Deepomatic's one with 'make'")
