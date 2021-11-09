#!/usr/bin/python

from node import Node
from game import Game
from util import Queue, Stack
from helpers import calculate_error
from random import randint

def bfs(g: Game):
    visited = set()
    queue = Queue()
    queue.push(Node(g.START_BOARD, g.ORDER))
    while queue.size() > 0:
        cur_node = queue.pop()
        if cur_node in visited:
            continue
        
        visited.add(cur_node)
        g.amount_of_visited_nodes += 1
        g.find_emptyxy(cur_node.board)

        if g.is_solved(cur_node.board):
            return cur_node.way, len(cur_node.way)-1
        
        cur_node.remove_illegal_moves(g.empty_xy)
        for move in cur_node.to_visit:
            g.amount_of_processed_nodes += 1
            cur_node.move(move, g.empty_xy)
            new_node = cur_node.children[move]
            queue.push(new_node)


def dfs(g: Game):
    visited = set()
    stack = Stack()
    stack.push(Node(g.START_BOARD, g.ORDER))
    while stack.size() > 0:
        cur_node = stack.pop()
        if cur_node in visited:
            continue
        
        visited.add(cur_node)
        g.amount_of_visited_nodes += 1
        g.find_emptyxy(cur_node.board)

        if g.is_solved(cur_node.board):
            return cur_node.way, len(cur_node.way)-1
        if len(cur_node.way) == g.MAX_DEPTH:
            continue

        cur_node.remove_illegal_moves(g.empty_xy)
        for move in cur_node.to_visit[::-1]:
            g.amount_of_processed_nodes += 1
            cur_node.move(move, g.empty_xy)
            new_node = cur_node.children[move]
            stack.push(new_node)

def astr(g: Game, heuristic):
    get_error = calculate_error(heuristic)
    cur_node = Node(g.START_BOARD, g.ORDER)
    while True:
        if g.is_solved(cur_node.board):
            return cur_node.way, len(cur_node.way)-1

        cur_node.remove_illegal_moves(g.empty_xy)
        for move in cur_node.to_visit:
            g.amount_of_processed_nodes += 1
            cur_node.move(move, g.empty_xy)
            temp_node = cur_node.children[move]
            error = get_error(temp_node.board, g.SOLVED_BOARD)
            cur_node.errors[move] = error
        min_value = min(cur_node.errors.values())
        tmp = [
            key for key in cur_node.errors
            if cur_node.errors[key] == min_value
        ]
        nr = randint(0, len(tmp)-1)
        next_move = tmp[nr]
        cur_node.move(next_move, g.empty_xy)
        cur_node = cur_node.children[next_move]
        g.find_emptyxy(cur_node.board)
        g.amount_of_visited_nodes += 1