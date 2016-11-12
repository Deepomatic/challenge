import random

def allowed_moves(board, color):
    """
        This is the first function you need to implement.

        Arguments:
        - board: The content of the board, represented as a list of strings.
                 The length of strings are the same as the length of the list,
                 which represents a 8x8 checkers board.
                 Each string is a row, from the top row (the black side) to the
                 bottom row (white side). The string are made of five possible
                 characters:
                 - '_' : an empty square
                 - 'b' : a square with a black disc
                 - 'B' : a square with a black king
                 - 'w' : a square with a white disc
                 - 'W' : a square with a white king
                 At the beginning of the game:
                 - the top left square of a board is always empty
                 - the square on it right always contains a black disc
        - color: the next player's color. It can be either 'b' for black or 'w'
                 for white.

        Return value:
        It must return a list of all the valid moves. Please refer to the
        README for a description of what are valid moves. A move is a list of
        all the squares visited by a disc or a king, from its initial position
        to its final position. The coordinates of the square must be specified
        using (row, column), with both 'row' and 'column' starting from 0 at
        the top left corner of the board (black side).

        Example:
        >> board = [
            '________',
            '__b_____',
            '_w_w____',
            '________',
            '_w______',
            '_____b__',
            '____w___',
            '___w____'
        ]

        The top-most black disc can chain two jumps and eat both left white
        discs or jump only over the right white disc. The other black disc
        cannot move because it does produces any capturing move.

        The output must thus be:
        >> allowed_moves(board, 'b')
        [
            [(1, 2), (3, 0), (5, 2)],
            [(1, 2), (3, 4)]
        ]
    """
    # TODO: Your turn now !
    return []

def play(board, color):
    """
        Play must return the next move to play.
        You can define here any strategy you would find suitable.
    """
    return random_play(board, color)

def random_play(board, color):
    """
        An example of play function based on allowed_moves.
    """
    moves = allowed_moves(board, color)
    # There will always be an allowed move
    # because otherwise the game is over and
    # 'play' would not be called by main.py
    return random.choice(moves)
