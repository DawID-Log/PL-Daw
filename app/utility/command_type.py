from enum import Enum

class CommandType(Enum):
    # Principal command
    TOKENIZE = "tokenize"
    EVALUATE = "evaluate"
    PARSE = "parse"