import re
import sys
import globals as glob
from os.path import exists


class Clargs:
    def __init__(self):
        if sys.argv[0] != 'main.py':
            print('Nonofficial execution.')
        self.args = sys.argv[1:]

    def is_valid_length(self) -> bool:
        return len(self.args) == glob.ARGUMENT_LENGTH

    def extract(self) -> None:
        self.method = self.args[0]
        self.strategy = self.args[1]
        self.source = self.args[2]
        self.solution_file = self.args[3]
        self.stat_file = self.args[4]
        self.filenames = [self.source, self.solution_file, self.stat_file]

    def is_valid_method(self) -> bool:
        return self.method in glob.METHODS

    def is_valid_strategy(self) -> bool:
        self.option = glob.METHOD_MAP[self.method]
        return glob.STRATS_DICT[self.option]['val'](self.strategy)

    def is_valid_files(self) -> bool:
        pattern = re.compile(glob.FILE_RE, re.IGNORECASE)
        val_name = all([re.fullmatch(pattern, f) for f in self.filenames])
        exist = exists(self.source)

        if not val_name:
            print('Files have wrong pattern', self.filenames)

        if not exist:
            print('Input file does not exist')

        return val_name and exist

    def is_valid(self) -> bool:
        if not self.is_valid_length():
            print('Incorrect number of arguments')
            return False
        self.extract()

        if not self.is_valid_method():
            print('Incorrect method name')
            return False

        if not self.is_valid_strategy():
            print('Incorrect strategy name')
            return False

        if self.is_valid_files():
            return True
        return False
