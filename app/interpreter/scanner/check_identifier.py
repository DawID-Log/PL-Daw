import re
from app.classes.token import Token
from app.utility.token_type import TokenType


def checkCharEqualToken(char, token, tokenName, tokens, isPrintable = True):
    if char.find(token) > -1:
        if isPrintable:
            token = Token(
                msg = f"{tokenName} {token} null",
                type = tokenName,
                lexeme = token,
                line = None,
                literal = "",
            )
            tokens.append(token)
        return True
    return False

def checkIdentifier(line, indexChar, tokens):
    if re.match(r"^[a-zA-Z_]*$", line[indexChar]):
        substring = line[indexChar:].split()
        if len(substring) > 0:
            resultId = substring[0]
            summer = 1

            if substring[0].find("(") > -1: resultId = substring[0][:substring[0].index("(")]
            elif substring[0].find(")") > -1: resultId = substring[0][:substring[0].index(")")]
            elif substring[0].find("{") > -1: resultId = substring[0][:substring[0].index("{")]
            elif substring[0].find("}") > -1: resultId = substring[0][:substring[0].index("}")]
            elif substring[0].find("@") > -1: resultId = substring[0][:substring[0].index("@")]
            elif substring[0].find("&") > -1: resultId = substring[0][:substring[0].index("&")]
            elif substring[0].find("$") > -1: resultId = substring[0][:substring[0].index("$")]
            elif substring[0].find("%") > -1: resultId = substring[0][:substring[0].index("%")]
            elif substring[0].find("#") > -1: resultId = substring[0][:substring[0].index("#")]
            
            if resultId == "":
                return 0
            
            token = Token(
                msg = f"{TokenType.IDENTIFIER.name} {resultId} null",
                type = TokenType.IDENTIFIER.name,
                lexeme = resultId,
                line = None,
                literal = "",
            )
            tokens.append(token)
            if resultId != substring[0]: summer = 0
            return len(resultId) + summer
    return 