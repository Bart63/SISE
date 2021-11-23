from clargs import Clargs
from methods import astr, bfs, dfs
from globals import BDFS_DICT, NANO_TO_MILI
from manager import Manager
from time import time_ns


def save_solved(stats, solution_file, statistic_file, delta_time):
    way, *other_stats = stats
    solution_length = len(way) if way != -1 else -1

    file = open(solution_file, 'w')
    file.write(str(solution_length))
    if way != -1:
        file.write('\n')
        file.write(''.join(way))
    file.close()

    file = open(statistic_file, 'w')
    file.write(str(solution_length))
    other_stats += [round(delta_time * NANO_TO_MILI, 3)]

    for s in other_stats:
        file.write('\n')
        file.write(str(s))
    file.close()


def main():
    cla = Clargs()
    if not cla.is_valid():
        return

    order = list(cla.strategy) if cla.option == 0 else BDFS_DICT['data']
    manager = Manager(order)

    with open(cla.source) as input_board:
        manager.gen_solved_board(
            list(map(int, input_board.readline().split()))
        )
        for line in input_board:
            manager.START_BOARD.append(line.split())

    start_time = time_ns()
    stats = bfs(manager) if cla.method == 'bfs' \
        else dfs(manager) if cla.method == 'dfs' \
        else astr(manager, cla.strategy)
    delta_time = time_ns() - start_time

    stats = [stats[0]] + [manager.visited_states_len, manager.processed_states_len] + [stats[1]]
    save_solved(stats, cla.solution_file, cla.stat_file, delta_time)


if __name__ == '__main__':
    main()
