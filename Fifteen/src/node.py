from __future__ import annotations
from globals import MOVEMENT, REVERSE_MOVEMENT_MAP
from typing import List


class Node:
    def __init__(self, current_board, order: List, way: List = None):
        self.board: List[List] = current_board
        self.way: List = way.copy() if way else []
        self.children = {}
        self.cost_f = 0
        self.to_visit: List = order.copy()
        if way:
            self.to_visit.remove(REVERSE_MOVEMENT_MAP[way[-1]])

    def __lt__(self, o) -> bool:
        if not isinstance(o, Node):
            raise Exception("Object is not an instance of Node")
        o: Node = o
        return self.cost_f < o.cost_f

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Node):
            return False
        o: Node = o
        return all(l1 == l2 for l1, l2 in zip(o.board, self.board))

    def __hash__(self):
        return hash(tuple(tuple(el for el in row) for row in self.board))

    def __repr__(self) -> str:
        return ''.join([
            ' '.join([str(el) for el in row]) + '\n'
            for row in self.board])

    def create_child(self, board_after_move, move: str, order):
        new_way = self.way + [move]
        child = Node(board_after_move, order, new_way)
        self.children[move] = child

    def move(self, move, empty, order):
        def swap_elements(board, p1, p2):
            board[p1[0]][p1[1]], board[p2[0]][p2[1]] = board[p2[0]][p2[1]], board[p1[0]][p1[1]]

        x, y = empty
        d_xy = MOVEMENT[move]

        tmp_array = []
        for row in self.board:
            tmp_array.append(row.copy())

        swap_elements(tmp_array, (x, y), (x + d_xy[0], y + d_xy[1]))
        self.create_child(tmp_array, move, order)

    def remove_illegal_moves(self, empty_xy):
        is_first_row = empty_xy[0] == 0
        is_first_col = empty_xy[1] == 0
        is_last_row = empty_xy[0] == len(self.board) - 1
        is_last_col = empty_xy[1] == len(self.board[0]) - 1

        to_remove = []

        if is_first_row:
            to_remove.append('U')
        elif is_last_row:
            to_remove.append('D')

        if is_first_col:
            to_remove.append('L')
        elif is_last_col:
            to_remove.append('R')

        for tr in to_remove:
            if tr in self.to_visit:
                self.to_visit.remove(tr)
