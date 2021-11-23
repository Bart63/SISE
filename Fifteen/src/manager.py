from helpers import get_index_of_value
import globals as glob


class Manager:
    SOLVED_BOARD = []
    START_BOARD = []
    empty_xy = (-1, -1)
    ORDER = []
    processed_states_len = 1
    visited_states_len = 1

    def __init__(self, order):
        self.ORDER = order
        self.MAX_DEPTH = glob.MAX_DEPTH

    def is_solved(self, current_board):
        return current_board == self.SOLVED_BOARD

    def gen_solved_board(self, dimensions):
        if len(dimensions) != 2:
            Exception("Incorrect number of dimensions")

        r, c = dimensions
        board = [[
                f'{j + i*c + 1}'
                for j in range(c)
            ] for i in range(r)
        ]
        board[r-1][c-1] = '0'
        self.SOLVED_BOARD = board

    def find_emptyxy(self, test_board):
        self.empty_xy = get_index_of_value(test_board, '0')
