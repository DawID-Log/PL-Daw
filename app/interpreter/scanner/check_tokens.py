import re
from app.classes.token import Token
from app.interpreter.scanner.check_identifier import checkCharEqualToken
from app.utility.token_type import TokenType


def checkSingleTokens(char, tokens):
    if checkCharEqualToken(char, "*", TokenType.STAR.name, tokens):
        return True
    elif checkCharEqualToken(char, ".", TokenType.DOT.name, tokens):
        return True
    elif checkCharEqualToken(char, ",", TokenType.COMMA.name, tokens):
        return True
    elif checkCharEqualToken(char, "+", TokenType.PLUS.name, tokens):
        return True
    elif checkCharEqualToken(char, "-", TokenType.MINUS.name, tokens):
        return True
    elif checkCharEqualToken(char, ";", TokenType.SEMICOLON.name, tokens):
        return True
    return False

def checkOperatorTokens(char, line, lineIndex, position, tokens):
    if checkCharEqualToken(char, "=", TokenType.EQUAL.name, tokens, False):
        if ((position + 1) < len(line)) and checkCharEqualToken(char + line[position + 1], "==", TokenType.EQUAL_EQUAL.name, tokens):
            return 2
        token = Token(
            msg = "EQUAL = null",
            type = TokenType.EQUAL.name,
            lexeme = "=",
            line = None,
            literal = "",
        )
        tokens.append(token)
        return 1
    elif checkCharEqualToken(char, "!", TokenType.BANG.name, tokens, False):
        if ((position + 1) < len(line)) and checkCharEqualToken(char + line[position + 1], "!=", TokenType.BANG_EQUAL.name, tokens):
            return 2
        token = Token(
            msg = "BANG ! null",
            type = TokenType.BANG.name,
            lexeme = "!",
            line = None,
            literal = "",
        )
        tokens.append(token)
        return 1
    elif checkCharEqualToken(char, "<", TokenType.LESS.name, tokens, False):
        if ((position + 1) < len(line)) and checkCharEqualToken(char + line[position + 1], "<=", TokenType.LESS_EQUAL.name, tokens):
            return 2
        token = Token(
            msg = "LESS < null",
            type = TokenType.LESS.name,
            lexeme = "<",
            line = None,
            literal = "",
        )
        tokens.append(token)
        return 1
    elif checkCharEqualToken(char, ">", TokenType.GREATER.name, tokens, False):
        if ((position + 1) < len(line)) and checkCharEqualToken(char + line[position + 1], ">=", TokenType.GREATER_EQUAL.name, tokens):
            return 2
        token = Token(
            msg = "GREATER > null",
            type = TokenType.GREATER.name,
            lexeme = ">",
            line = None,
            literal = "",
        )
        tokens.append(token)
        return 1
    elif checkCharEqualToken(char, "/", TokenType.SLASH.name, tokens, False):
        if ((position + 1) < len(line)) and checkCharEqualToken(char + line[position + 1], "//", TokenType.COMMENT.name, tokens, False):
            return len(line)
        token = Token(
            msg = "SLASH / null",
            type = TokenType.SLASH.name,
            lexeme = "/",
            line = None,
            literal = "",
        )
        tokens.append(token)
        return 1
    elif checkCharEqualToken(char, "\"", TokenType.STRING.name, tokens, False):
        actualPosition = position + 1
        subStringAct = line[actualPosition:]
        stringResult = ""

        if subStringAct.find("\"") == -1:
            return len(line)
        
        actualPosition = subStringAct.index("\"")
        stringResult = subStringAct[0:actualPosition]

        token = Token(
            msg = f"{TokenType.STRING.name} \"{stringResult}\" {stringResult}",
            type = TokenType.STRING.name,
            lexeme = stringResult,
            literal = stringResult,
            line = None,
        )
        tokens.append(token)
        return actualPosition + 2
    return 0

def checkNumberTokens(char, line, lineIndex, position, tokens):
    if char.isnumeric():
        actualPosition = position
        subStringAct = line[actualPosition:]
        numberResult = 0
        stringResult = ""
        lenResult = 1
        subStringNum = re.findall(r"\d+\.\d+", subStringAct)
        if len(subStringNum) > 0:
            numberResult = subStringNum[0]
            stringResult = subStringNum[0]
            lenResult = len(stringResult)
            if subStringNum[0].find(".00") > -1:
                stringResult = subStringNum[0][:len(subStringNum[0]) - 1]
                lenResult = len(stringResult) + 1
        else:
            subStringNum = re.findall(r"\d+\.", subStringAct)
            if len(subStringNum) > 0: 
                lenResult = len(subStringNum[0]) - 1
                numberResult = int(subStringNum[0][:lenResult])
                stringResult = subStringNum[0] + "0"
            else:
                subStringNum = re.findall(r"\d+", subStringAct)
                if len(subStringNum) > 0: 
                    numberResult = subStringNum[0]
                    stringResult = subStringNum[0] + ".0"
                    lenResult = len(stringResult) - 2
        
        token = Token(
            msg = f"{TokenType.NUMBER.name} {numberResult} {stringResult}",
            type = TokenType.NUMBER.name,
            lexeme = numberResult,
            line = None,
            literal = stringResult,
        )
        tokens.append(token)
        return lenResult
    return 0

def checkReservedToken(line, indexChar, tokens):
    reservedTokens = [
        TokenType.AND.name, 
        TokenType.CLASS.name, 
        TokenType.ELSE.name, 
        TokenType.FALSE.name, 
        TokenType.FOR.name, 
        TokenType.FUN.name, 
        TokenType.IF.name,
        TokenType.NIL.name, 
        TokenType.OR.name, 
        TokenType.PRINT.name, 
        TokenType.RETURN.name, 
        TokenType.SUPER.name, 
        TokenType.THIS.name, 
        TokenType.TRUE.name, 
        TokenType.VAR.name, 
        TokenType.WHILE.name]
    substring = line[indexChar:].split()
    for token in reservedTokens:
        if len(substring) > 0 and token.lower() == substring[0]:
            tokens.append(Token(
                msg = f"{token} {substring[0]} null",
                type = token,
                lexeme = substring[0],
                line = None,
                literal = "",
            ))
            return len(token)
    return 0