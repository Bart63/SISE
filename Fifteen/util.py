from node import Node

class DataStructure():
    def __init__(self):
        self.struct = []

    def push(self, value):
        self.struct.append(value)

    def size(self):
        return len(self.struct)

class Queue(DataStructure):
    def __init__(self):
        super(Queue, self).__init__()

    def pop(self) -> Node:
        if self.size() > 0:
            return self.struct.pop(0)
        return None

class Stack(DataStructure):
    def __init__(self):
        super(Stack, self).__init__()

    def pop(self) -> Node:
        if self.size() > 0:
            return self.struct.pop()
        return None