from app.interpreter.scanner.check_identifier import checkCharEqualToken
from app.utility.token_type import TokenType

def checkParentheses(char, tokens):
    if checkCharEqualToken(char, "(", TokenType.LEFT_PAREN.name, tokens):
        return True
    elif checkCharEqualToken(char, ")", TokenType.RIGHT_PAREN.name, tokens):
        return True
    return False

def checkBraces(char, tokens):
    if checkCharEqualToken(char, "{", TokenType.LEFT_BRACE.name, tokens):
        return True
    elif checkCharEqualToken(char, "}", TokenType.RIGHT_BRACE.name, tokens):
        return True
    return False