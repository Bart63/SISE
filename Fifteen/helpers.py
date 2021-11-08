#!/usr/bin/python

def get_index_of_value(board, val):
    for i, row in enumerate(board):
        if val in row:
            return i, row.index(val)

def generate_error_list(current_board, solved_board):
    return [sum([
            abs(curr-target) 
            for curr, target in zip((row_indx, col_indx), get_index_of_value(solved_board, el))
        ])
        for row_indx, row in enumerate(current_board)
        for col_indx, el in enumerate(row)
    ]

def calculate_error_manh(current_board, solved_board):
    manh_error = 0
    for index_row, row in enumerate(current_board):
        for index_col, elem in enumerate(row):
            target_row, target_col = get_index_of_value(solved_board, elem)
            manh_error += abs(index_row - target_row) + abs(index_col - target_col)
    return manh_error

def calculate_error_hamm(current_board, solved_board):
    return sum([
        el!=0 for el in generate_error_list(current_board, solved_board)
    ])

def get_calculate_error(heuristic):
    return calculate_error_manh if heuristic == 'manh' else calculate_error_hamm