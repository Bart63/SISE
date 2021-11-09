#!/usr/bin/python

from typing import List

def get_index_of_value(board: List[List], val):
    for i, row in enumerate(board):
        if val in row:
            return i, row.index(val)

def get_error_list(current_board: List[List], solved_board: List[List]):
    return [sum([
            abs(curr-target) 
            for curr, target in zip((row_indx, col_indx), get_index_of_value(solved_board, el))
        ])
        for row_indx, row in enumerate(current_board)
        for col_indx, el in enumerate(row)
    ]

def calculate_error_manh(current_board: List[List], solved_board: List[List]):
    return sum(get_error_list(current_board, solved_board))

def calculate_error_hamm(current_board: List[List], solved_board: List[List]):
    return sum([
        el!=0 for el in get_error_list(current_board, solved_board)
    ])

def calculate_error(heuristic: str):
    return calculate_error_manh if heuristic == 'manh' else calculate_error_hamm