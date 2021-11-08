#!/usr/bin/python
from __future__ import annotations
from globals import MOVEMENT, ADD_ELEMTWISE, REVERSE_MOVEMENT_MAP

class Node:
    def __init__(self, current_board, order, way=[]):
        self.board:list = current_board
        self.way = way.copy()
        self.children:dict[str, Node] = {}
        self.errors = {}
        self.default_order = order
        self.to_visit:list = order.copy()
        if way:
            self.to_visit.remove(REVERSE_MOVEMENT_MAP[way[-1]])

    def get_child(self, child) -> Node:
        return self.children[child]

    def create_child(self, board_after_move, move):
        new_way = self.way + [move]
        child = Node(board_after_move, self.default_order, new_way)
        self.children[move] = child

    def make_move(self, move, empty):
        def swap_elements(board, p1, p2):
            board[p1[0]][p1[1]], board[p2[0]][p2[1]] = board[p2[0]][p2[1]], board[p1[0]][p1[1]]
        
        x, y = empty
        d_xy = MOVEMENT[move]

        tmp_array = []
        for row in self.board:
            tmp_array.append(row.copy())

        swap_elements(tmp_array, (x, y), (x+d_xy[0], y+d_xy[1]))
        self.create_child(tmp_array, move)
        
        next_empty = tuple(map(ADD_ELEMTWISE, empty, d_xy))
        return next_empty

    def remove_ways_to_out_of_board(self, empty_xy):
        is_first_row = empty_xy[0] == 0
        is_first_col = empty_xy[1] == 0
        is_last_row = empty_xy[0] == len(self.board)-1
        is_last_col = empty_xy[1] == len(self.board[0])-1
        
        if is_first_row:
            self.to_visit.remove('U')
        elif is_last_row:
            self.to_visit.remove('D')

        if is_first_col:
            self.to_visit.remove('L')
        elif is_last_col:
            self.to_visit.remove('R')