class Token:
    def __init__(self, type, lexeme, msg, literal, line, error=False):
        self.type = type
        self.lexeme = lexeme
        self.msg = msg
        self.literal = literal
        self.line = line
        self.error = error

    def __str__(self):
        return self.type + " " + self.lexeme + " " + self.literal
        