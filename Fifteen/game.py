#!/usr/bin/python

from globals import MOVEMENT, ADD_ELEMTWISE
from helpers import get_index_of_value

class Game():
    MAX_DEPTH = 20
    SOLVED_BOARD = []
    START_BOARD = []
    empty_xy = (-1, -1)
    ORDER = []
    amount_of_processed_nodes = 1
    amount_of_visited_nodes = 1

    def __init__(self, order):
        self.ORDER = order

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

    def change_position_of_blank_field(self, last_move):
        negative_move = tuple(-t for t in MOVEMENT[last_move])
        self.empty_xy = tuple(map(ADD_ELEMTWISE, self.empty_xy, negative_move))

    def find_and_set_empty_field(self, test_board):
        self.empty_xy = get_index_of_value(test_board, '0')