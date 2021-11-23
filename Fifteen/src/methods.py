from node import Node
from manager import Manager
from util import Queue, Stack
from queue import PriorityQueue
from helpers import calculate_cost


def bfs(manager: Manager):
    max_depth = 0
    processed = set()
    queue = Queue()
    queue.push(Node(manager.START_BOARD, manager.ORDER))

    while len(queue) > 0:
        cur_node = queue.pop()
        if len(cur_node.way) > max_depth:
            max_depth = len(cur_node.way)

        manager.find_emptyxy(cur_node.board)
        cur_node.remove_illegal_moves(manager.empty_xy)
        processed.add(cur_node)

        for move in cur_node.to_visit:
            cur_node.move(move, manager.empty_xy, manager.ORDER)
            new_node:Node = cur_node.children[move]
            if new_node in processed or new_node in queue:
                continue
            queue.push(new_node)

            if not manager.is_solved(new_node.board):
                continue
            manager.processed_states_len = len(processed)
            manager.visited_states_len = len(processed) + len(queue)
            return new_node.way, len(new_node.way)
    return -1, max_depth


def dfs(manager: Manager):
    max_depth = 0
    processed = set()
    stack = Stack()
    recorded_depth = {}
    not_processed = set()
    stack.push(Node(manager.START_BOARD, manager.ORDER))

    while len(stack) > 0:
        cur_node = stack.pop()
        if cur_node in processed and len(cur_node.way) >= recorded_depth[hash(cur_node)]:
            continue

        recorded_depth[hash(cur_node)] = len(cur_node.way)
        if len(cur_node.way) > max_depth:
            max_depth = len(cur_node.way)

        if len(cur_node.way) == manager.MAX_DEPTH:
            not_processed.add(cur_node)
            continue

        manager.find_emptyxy(cur_node.board)
        cur_node.remove_illegal_moves(manager.empty_xy)
        processed.add(cur_node)
        
        for move in cur_node.to_visit[::-1]:
            cur_node.move(move, manager.empty_xy, manager.ORDER)
            new_node:Node = cur_node.children[move]
            stack.push(new_node)

            if not manager.is_solved(new_node.board):
                continue
            manager.processed_states_len = len(processed)
            visited_nodes = processed.union(not_processed).union(stack)
            manager.visited_states_len = len(visited_nodes)
            if len(new_node.way) > max_depth:
                max_depth = len(new_node.way)
            return new_node.way, max_depth
    return -1, max_depth


def astr(manager: Manager, heuristic):
    get_cost = calculate_cost(heuristic)
    max_depth = 0
    open_list = PriorityQueue()
    closed_list = set()
    open_list.put(Node(manager.START_BOARD, manager.ORDER))

    while not open_list.empty():
        cur_node:Node = open_list.get()
        if len(cur_node.way) > max_depth:
            max_depth = len(cur_node.way)

        if manager.is_solved(cur_node.board):
            manager.processed_states_len = len(closed_list)
            queue_elements = set([cur_node])
            while not open_list.empty():
                queue_elements.add(open_list.get())
            manager.visited_states_len = len(closed_list) + len(queue_elements)
            return cur_node.way, max_depth
        
        closed_list.add(cur_node)
        manager.find_emptyxy(cur_node.board)
        cur_node.remove_illegal_moves(manager.empty_xy)

        for move in cur_node.to_visit:
            cur_node.move(move, manager.empty_xy, manager.ORDER)
            new_node: Node = cur_node.children[move]
            if new_node in closed_list:
                continue

            cost_g = get_cost(manager.START_BOARD, new_node.board)
            cost_h = get_cost(new_node.board, manager.SOLVED_BOARD)
            new_node.cost_f = cost_g + cost_h
            open_list.put(new_node)
    return -1, max_depth
