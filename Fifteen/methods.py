#!/usr/bin/python

from node import Node
from game import Game
import random
from helpers import get_calculate_error
from util import Queue, Stack
import time

def bfs(g: Game):
    visited = set()
    queue = Queue()
    queue.push(Node(g.START_BOARD, g.ORDER))
    while queue.size() > 0:
        cur_node = queue.pop()
        g.find_and_set_empty_field(cur_node.board)

        if cur_node in visited:
            continue
        if g.is_solved(cur_node.board):
            return cur_node.way, len(cur_node.way)-1
        
        visited.add(cur_node)
        cur_node.remove_ways_to_out_of_board(g.empty_xy)

        for move in cur_node.to_visit:
            g.amount_of_processed_nodes += 1
            g.empty_xy = cur_node.make_move(move, g.empty_xy)
            new_node = cur_node.children[move]
            queue.push(new_node)
            g.change_position_of_blank_field(new_node.way[-1])
        g.amount_of_visited_nodes += 1


def dfs(g: Game, start_time):
    visited = set()
    stack = Stack()
    stack.push(Node(g.START_BOARD, g.ORDER))
    while stack.size() > 0:
        cur_node = stack.pop()
        
        if cur_node in visited:
            continue
        
        if g.is_solved(cur_node.board):
            return cur_node.way, len(cur_node.way)-1

        visited.add(cur_node)
        g.amount_of_visited_nodes += 1

        if len(cur_node.way) == g.MAX_DEPTH:
            continue

        g.find_and_set_empty_field(cur_node.board)
        cur_node.remove_ways_to_out_of_board(g.empty_xy)

        for move in cur_node.to_visit[::-1]:
            g.amount_of_processed_nodes += 1
            g.empty_xy = cur_node.make_move(move, g.empty_xy)
            new_node = cur_node.children[move]
            stack.push(new_node)
            g.change_position_of_blank_field(new_node.way[-1])
        
        if stack.size()==0 or time.time() - start_time > g.MAX_DEPTH:
            return -1, len(cur_node.way)-1


def astr(g: Game, heuristic):
    calculate_error = get_calculate_error(heuristic)
    cur_node = Node(g.START_BOARD, g.ORDER)
    while True:
        if g.is_solved(cur_node.board):
            return cur_node.way, len(cur_node.way)-1

        cur_node.remove_ways_to_out_of_board(g.empty_xy)
        for move in cur_node.to_visit:
            g.amount_of_processed_nodes += 1
            g.empty_xy = cur_node.make_move(move, g.empty_xy)
            temp_node = cur_node.children[move]
            error = calculate_error(temp_node.board, g.SOLVED_BOARD)
            g.find_and_set_empty_field(cur_node.board)
            cur_node.errors[move] = error
        min_value = min(cur_node.errors.values())
        tmp = [
            key for key in cur_node.errors
            if cur_node.errors[key] == min_value
        ]
        nr = random.randint(0, len(tmp)-1)
        next_move = tmp[nr]
        g.empty_xy = cur_node.make_move(next_move, g.empty_xy)
        cur_node = cur_node.children[next_move]
        g.amount_of_visited_nodes += 1