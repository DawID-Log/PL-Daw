from app.classes.token import Token
from app.interpreter.scanner.check_identifier import checkIdentifier
from app.interpreter.scanner.check_parentheses import checkBraces, checkParentheses
from app.interpreter.scanner.check_tokens import checkNumberTokens, checkOperatorTokens, checkReservedToken, checkSingleTokens
from app.utility.managment_error import checkCharEqualErrorToken, checkUnterminatedString
from app.utility.token_type import TokenType

def startScanner(file_contents):
    contents = file_contents.split("\n")
    statusError = []
    tokens: list[Token] = []
    for line in contents:
        lineIndex = contents.index(line)
        indexChar = 0

        while indexChar < len(line):
            if line[indexChar] == " ": 
                indexChar += 1
                continue

            # VARIABLE DECLARATION
            char = line[indexChar]
            statusFlow = 0
            statusPipeline = []
            checkErrorToken(char, lineIndex, statusError)
            statusPipeline.append(checkParentheses(char, tokens))
            statusPipeline.append(checkBraces(char, tokens))
            statusPipeline.append(checkSingleTokens(char, tokens))
            statusFlow = checkOperatorTokens(char, line, lineIndex, indexChar, tokens)
            if not(statusPipeline.count(True) > 0):
                if statusFlow == 0: statusFlow = checkReservedToken(line, indexChar, tokens)
                if statusFlow == 0: statusFlow = checkNumberTokens(char, line, lineIndex, indexChar, tokens)
                if statusFlow == 0: statusFlow = checkIdentifier(line, indexChar, tokens)

            # CHECK NEXT STEP
            if statusFlow == 0 or statusFlow == None: statusFlow = 1
            indexChar += statusFlow
        statusError.append(checkUnterminatedString(line, lineIndex))
    endOfFile(tokens, statusError)
    return tokens

def checkErrorToken(char, numberLine, statusError):
    statusError.append(checkCharEqualErrorToken(char, numberLine, "$"))
    statusError.append(checkCharEqualErrorToken(char, numberLine, "#"))
    statusError.append(checkCharEqualErrorToken(char, numberLine, "@"))
    statusError.append(checkCharEqualErrorToken(char, numberLine, "%"))
    statusError.append(checkCharEqualErrorToken(char, numberLine, "&"))

def endOfFile(tokens = [], statusError = []):
    token = Token(
        msg = TokenType.EOF.name + "  null",
        type = TokenType.EOF.name,
        lexeme = " ",
        line = None,
        literal = "",
        error = True in statusError
    )
    tokens.append(token)        