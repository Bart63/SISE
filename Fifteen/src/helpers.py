from typing import List


def get_index_of_value(board: List[List], val):
    for i, row in enumerate(board):
        if val in row:
            return i, row.index(val)


def get_distance_list(current_board: List[List], target_board: List[List]):
    er_li = [sum([
        abs(curr - target)
        for curr, target in zip((row_idx, col_idx), get_index_of_value(target_board, el))
        if el != '0'
    ])
        for row_idx, row in enumerate(current_board)
        for col_idx, el in enumerate(row)
    ]
    return er_li


def calculate_cost_manh(current_board: List[List], target_board: List[List]):
    return sum(get_distance_list(current_board, target_board))


def calculate_cost_hamm(current_board: List[List], target_board: List[List]):
    return sum([
        el != 0 for el in get_distance_list(current_board, target_board)
    ])


def calculate_cost(heuristic: str):
    return calculate_cost_manh if heuristic == 'manh' else calculate_cost_hamm
