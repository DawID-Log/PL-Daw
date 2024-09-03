from enum import Enum

def acceptedLiterals(type = "base"): 
    if type == "base":
        return [
            TokenType.NUMBER.name,
            TokenType.IDENTIFIER.name,
            TokenType.STRING.name,
            TokenType.TRUE.name, 
            TokenType.FALSE.name,       
            TokenType.NIL.name, 
        ]
    elif type == "unaryOp":
        return [
            TokenType.MINUS.name,
            TokenType.BANG.name
        ]
    elif type == "binaryOp":
        return [
            TokenType.MINUS.name,
            TokenType.PLUS.name,
            TokenType.STAR.name,
            TokenType.SLASH.name,
            TokenType.GREATER.name,
            TokenType.GREATER_EQUAL.name,
            TokenType.LESS.name,
            TokenType.LESS_EQUAL.name,
            TokenType.BANG_EQUAL.name,
            TokenType.EQUAL_EQUAL.name
        ]
    elif type == "numericExpression":
        return [
            TokenType.NUMBER.name,
            TokenType.MINUS.name,
            TokenType.PLUS.name,
            TokenType.STAR.name,
            TokenType.SLASH.name,
            TokenType.GREATER.name,
            TokenType.GREATER_EQUAL.name,
            TokenType.LESS.name,
            TokenType.LESS_EQUAL.name,
            TokenType.BANG_EQUAL.name,
            TokenType.EQUAL_EQUAL.name
        ]

class TokenType(Enum):
    # Single-character tokens.
    LEFT_PAREN = "(", 
    RIGHT_PAREN = ")", 
    LEFT_BRACE = "{", 
    RIGHT_BRACE = "}", 
    COMMA = "COMMA", 
    DOT = "DOT", 
    MINUS = "MINUS",
    PLUS = "PLUS", 
    SEMICOLON = "SEMICOLON", 
    SLASH = "SLASH", 
    STAR = "STAR",

    # One or two character tokens.
    BANG = "BANG", 
    BANG_EQUAL = "BANG_EQUAL",
    EQUAL = "EQUAL", 
    EQUAL_EQUAL = "EQUAL_EQUAL",
    GREATER = "GREATER", 
    GREATER_EQUAL = "GREATER_EQUAL",
    LESS = "LESS", 
    LESS_EQUAL = "LESS_EQUAL",
    COMMENT = "COMMENT"

    # Literals.
    IDENTIFIER = "IDENTIFIER", 
    STRING = "STRING", 
    NUMBER = "NUMBER",

    # Keywords.
    AND = "AND", 
    CLASS = "CLASS", 
    ELSE = "ELSE", 
    FALSE = "FALSE", 
    FUN = "FUN", 
    FOR = "FOR", 
    IF = "IF", 
    NIL = "NIL", 
    OR = "OR",
    PRINT = "PRINT", 
    RETURN = "RETURN", 
    SUPER = "SUPER", 
    THIS = "THIS", 
    TRUE = "TRUE", 
    VAR = "VAR", 
    WHILE = "WHILE",

    EOF = "EOF"