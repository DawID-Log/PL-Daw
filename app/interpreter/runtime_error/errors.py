from contextvars import Token

def checkNumberUnaryOp(token: Token, rightOp):
    if rightOp.isdigit(): return
    raise RuntimeError(token, "Operand must be a number.")


def checkNumberBinaryOp(token: Token, leftOp, rightOp):
    if leftOp.isdigit() and rightOp.isdigit(): return
    raise RuntimeError(token, "Operands must be a number.")

def checkStringBinaryOp(token: Token, leftOp, rightOp):
    if not (leftOp.isdigit() and rightOp.isdigit()): return
    raise RuntimeError(token, "Operands must be a string.")
