ARGUMENT_LENGTH = 5
MAX_DEPTH = 20
NANO_TO_MILI = 0.000001

METHODS = ['bfs', 'dfs', 'astr']

METHOD_MAP = {
    'bfs': 0,
    'dfs': 0,
    'astr': 1
}

BDFS_DICT = {
    'data': ['L', 'R', 'U', 'D'],
    'val': lambda x: set(x) == set(BDFS_DICT['data'])
}

ASTR_DICT = {
    'data': ['hamm', 'manh'],
    'val': lambda x: x in ASTR_DICT['data']
}

STRATS_DICT = {
    0: BDFS_DICT,
    1: ASTR_DICT
}

FILE_RE = r'^[0-9]+[x][0-9]+_[0-9]+_[0-9]+[a-zA-Z_]*.txt'

MOVEMENT = {
    'R': (0, 1),
    'L': (0, -1),
    'U': (-1, 0),
    'D': (1, 0)
}

REVERSE_MOVEMENT_MAP = {
    'R': 'L',
    'L': 'R',
    'U': 'D',
    'D': 'U'
}
