from app.interpreter.evaluating_exp.converter import objToString

class EvaluateToken:
    def __init__(self, type, result, line, isPrintable=False, error=""):
        self.type = type
        self.result = result
        self.line = line
        self.isPrintable = isPrintable
        self.error = error

    def __str__(self):
        return self.type + " " + objToString(self.result)