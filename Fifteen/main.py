#!/usr/bin/python

from clargs import Clargs
from methods import astr, bfs, dfs
from globals import BDFS_DICT
from game import Game
import time

def prepare_solution(stats, solution_file, statistic_file, s_time):
    way, *other_stats = stats
    solution_length = len(way) if way != -1 else -1
    
    file = open(solution_file, 'w+')
    file.write(str(solution_length))
    if way != -1:
        file.write('\n')
        file.write(''.join(way))
    file.close()

    file = open(statistic_file, 'w+')
    file.write(str(solution_length))
    other_stats += [round((time.time() - s_time) * 1000, 3)]
    
    for s in other_stats:
        file.write('\n')
        file.write(str(s))
    file.close()

def main():
    cla = Clargs()
    if not cla.is_valid():
        return

    order = list(cla.strategy) if cla.option==0 else BDFS_DICT['data']
    g = Game(order)

    with open(cla.source) as input_board:
        g.gen_solved_board(
            list(map(int, input_board.readline().split()))
        )
        for line in input_board:
            g.START_BOARD.append(line.split())
                      
    g.find_and_set_empty_field(g.START_BOARD)
    
    start_time = time.time()
    stats = bfs(g) if cla.method=='bfs' \
        else dfs(g, start_time) if cla.method=='dfs' \
        else astr(g, cla.strategy)

    stats = [stats[0]] + [g.amount_of_visited_nodes, g.amount_of_processed_nodes] + [stats[1]]
    prepare_solution(stats, cla.solution_file, cla.stat_file, start_time)

if __name__ == '__main__':
    main()