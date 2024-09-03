import sys

class SystemArgument:
    def __init__(self):
        self.command = sys.argv[1]
        self.filename = sys.argv[2]