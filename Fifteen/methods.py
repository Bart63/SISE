#!/usr/bin/python

from node import Node
from game import Game
from util import Queue, Stack
from helpers import calculate_error, add_to_open

def bfs(g: Game):
    max_depth = 0
    visited = set()
    queue = Queue()
    queue.push(Node(g.START_BOARD, g.ORDER))
    while queue.size() > 0:
        cur_node = queue.pop()
        if cur_node in visited:
            continue
        max_depth = len(cur_node.way) if len(cur_node.way)>max_depth else max_depth
        visited.add(cur_node)
        g.find_emptyxy(cur_node.board)
        if g.is_solved(cur_node.board):
            return cur_node.way, len(cur_node.way)-1
        cur_node.remove_illegal_moves(g.empty_xy)
        for move in cur_node.to_visit:
            g.amount_of_processed_nodes += 1
            cur_node.move(move, g.empty_xy)
            new_node = cur_node.children[move]
            queue.push(new_node)
        g.amount_of_visited_nodes += 1
    return -1, max_depth

def dfs(g: Game):
    max_depth = 0
    visited = set()
    stack = Stack()
    stack.push(Node(g.START_BOARD, g.ORDER))    
    while stack.size() > 0:
        cur_node = stack.pop()
        if cur_node in visited:
            continue
        max_depth = len(cur_node.way) if len(cur_node.way)>max_depth else max_depth
        visited.add(cur_node)
        g.find_emptyxy(cur_node.board)
        if g.is_solved(cur_node.board):
            return cur_node.way, max_depth
        if len(cur_node.way) == g.MAX_DEPTH:
            continue
        cur_node.remove_illegal_moves(g.empty_xy)
        for move in cur_node.to_visit[::-1]:
            g.amount_of_processed_nodes += 1
            cur_node.move(move, g.empty_xy)
            new_node = cur_node.children[move]
            stack.push(new_node)
        g.amount_of_visited_nodes += 1
    return -1, max_depth

def astr(g: Game, heuristic):
    get_error = calculate_error(heuristic)
    max_depth = 0
    open = []
    closed = set()
    open.append(Node(g.START_BOARD, g.ORDER))
    while len(open)>0:
        open.sort()
        cur_node:Node = open.pop(0)
        max_depth = len(cur_node.way) if len(cur_node.way)>max_depth else max_depth
        closed.add(cur_node)
        if g.is_solved(cur_node.board):
            return cur_node.way, max_depth
        g.find_emptyxy(cur_node.board)
        cur_node.remove_illegal_moves(g.empty_xy)
        for move in cur_node.to_visit:
            g.amount_of_processed_nodes += 1
            cur_node.move(move, g.empty_xy)
            neighbor_node:Node = cur_node.children[move]
            if(neighbor_node in closed):
                continue
            cost_g = get_error(g.START_BOARD, neighbor_node.board)
            cost_h = get_error(neighbor_node.board, g.SOLVED_BOARD)
            neighbor_node.costs['f'] = cost_g + cost_h
            if add_to_open(open, neighbor_node):
                open.append(neighbor_node)
        g.amount_of_visited_nodes += 1
    return -1, max_depth