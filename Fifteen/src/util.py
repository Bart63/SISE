from node import Node
from typing import List, Union


class DataStructure:
    def __init__(self):
        self.struct:List[Node] = []

    def __iter__(self):
        for el in self.struct:
            yield el

    def __repr__(self) -> str:
        return '\n'.join(str(el) for el in self.struct)

    def push(self, value):
        self.struct.append(value)

    def __len__(self) -> int:
        return len(self.struct)


class Queue(DataStructure):
    def __init__(self):
        super(Queue, self).__init__()

    def pop(self) -> Union[Node, None]:
        if self.__len__() > 0:
            return self.struct.pop(0)
        return None


class Stack(DataStructure):
    def __init__(self):
        super(Stack, self).__init__()

    def pop(self) -> Union[Node, None]:
        if self.__len__() > 0:
            return self.struct.pop()
        return None
