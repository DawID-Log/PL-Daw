from contextvars import Token
from app.interpreter.evaluating_exp.boolean import isEqual
from app.interpreter.runtime_error.errors import checkNumberBinaryOp, checkStringBinaryOp
from app.utility.token_type import TokenType

def evaluateBinaryOperators(token: Token, leftToken: Token, rightToken: Token):
    if leftToken.lexeme.isdigit() or rightToken.lexeme.isdigit():
        return evaluateNumbers(token, leftToken.lexeme, rightToken.lexeme)
    else:
        return evaluateString(token, leftToken.lexeme, rightToken.lexeme)

def evaluateNumbers(token: Token, leftOp, rightOp):
    checkNumberBinaryOp(token, leftOp, rightOp)
    leftOpConverted = float(leftOp)
    rightOpConverted = float(rightOp)
    if token.type == TokenType.MINUS.name:
        return leftOpConverted - rightOpConverted
    elif token.type == TokenType.SLASH.name:
        return leftOpConverted / rightOpConverted
    elif token.type == TokenType.STAR.name:
       return leftOpConverted * rightOpConverted
    elif token.type == TokenType.PLUS.name:
        return leftOpConverted + rightOpConverted
    elif token.type  == TokenType.GREATER:
        return leftOpConverted > rightOpConverted
    elif token.type  == TokenType.GREATER_EQUAL:
        return leftOpConverted >= rightOpConverted
    elif token.type  == TokenType.LESS:
        return leftOpConverted < rightOpConverted
    elif token.type  == TokenType.LESS_EQUAL:
        return leftOpConverted <= rightOpConverted
    elif token.type == TokenType.BANG_EQUAL:
        return not isEqual(leftOpConverted, rightOpConverted)
    elif token.type  == TokenType.EQUAL_EQUAL:
        return isEqual(leftOpConverted, rightOpConverted)    
    return None

def evaluateString(token: Token, leftOp, rightOp):
    checkStringBinaryOp(token, leftOp, rightOp)
    if token.type == TokenType.PLUS.name:
        return leftOp + rightOp
    