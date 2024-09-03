from contextvars import Token
from app.interpreter.evaluating_exp.boolean import isTruthy
from app.interpreter.runtime_error.errors import checkNumberUnaryOp
from app.utility.token_type import TokenType, acceptedLiterals

def evaluateUnaryOperators(token: Token, tokens, index):
    if index + 2 < len(tokens) and tokens[index + 1].type in acceptedLiterals("unaryOp"):
        return doubleOperator(token, tokens[index + 1], tokens[index + 2].lexeme)
    else: 
        return numberOperation(token, tokens[index + 1].lexeme)

def numberOperation(token: Token, rightOp):
    if token.type == TokenType.MINUS.name:        
        checkNumberUnaryOp(token, rightOp)
        return -float(rightOp)
    if token.type == TokenType.BANG.name:
        return not isTruthy(rightOp)
    return None

def doubleOperator(firstToken: Token, secondtoken: Token, rightOp):
    if firstToken.type == TokenType.BANG.name and secondtoken.type == TokenType.BANG.name:
        return isTruthy(rightOp)