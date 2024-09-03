from app.classes.evaluate_token import EvaluateToken
from app.classes.token import Token
from app.interpreter.evaluating_exp.binary_operators import evaluateBinaryOperators
from app.interpreter.evaluating_exp.converter import objToString
from app.interpreter.evaluating_exp.unary_operators import evaluateUnaryOperators
from app.utility.token_type import TokenType, acceptedLiterals


def evaluatingExpressions(tokens):
    evaluateTokens: list[EvaluateToken] = []
    openParent = []
    closeParent = []
    numericExpressions = []
    isBinaryExpression = False

    for token in tokens:  
        if tokens.index(token) - 1 >= 0 and token.type in acceptedLiterals("binaryOp") and tokens.index(token) + 1 < len(tokens):
            isBinaryExpression = True
            break

    if isBinaryExpression:
        # Scope paren
        for token in tokens:
            if token.type == TokenType.LEFT_PAREN.name:
                openParent.append(tokens.index(token))
            elif token.type == TokenType.RIGHT_PAREN.name:
                closeParent.append(tokens.index(token))


        # Expression
        expression: list[Token] = []
        tokensSub = tokens[closeParent[0]:] if len(closeParent) != 0 else tokens
        for token in tokensSub:
            if token.type in acceptedLiterals("numericExpression"):
                expression.append(token)
            elif len(expression) != 0:
                numericExpressions.append(expression)
        
        if not (expression in numericExpressions) and len(expression) != 0:
            numericExpressions.append(expression)
        
        # Evaluate Number
        posEvaluate = 0
        tokensToBeEvaluated = []
        while len(openParent) != 0:
            tokenEvaluate: EvaluateToken = EvaluateToken("", "", "")
            posEvaluate = openParent[len(openParent) - 1] + 1
            result = 0

            while posEvaluate < closeParent[0]:
                token = tokens[posEvaluate]
                if posEvaluate - 1 >= 0 and token.type in acceptedLiterals("binaryOp") and posEvaluate + 1 < len(tokens):
                    lastTokenEvaluated = Token(token.type, objToString(result), "", "", "") if result != 0 else tokens[posEvaluate - 1]
                    rigthLastTokenEvaluated = tokens[posEvaluate + 1]
                    if len(tokensToBeEvaluated) != 0 and tokens[posEvaluate + 1].type == TokenType.LEFT_PAREN.name:
                        rigthLastTokenEvaluated = Token(token.type, objToString(tokensToBeEvaluated[len(tokensToBeEvaluated) - 1].result), "", "", "")
                        posEvaluate = closeParent[0]
                    result = evaluateBinaryOperators(token, lastTokenEvaluated, rigthLastTokenEvaluated)
                    
                posEvaluate += 1
            del openParent[-1]
            closeParent.pop(0)
            
            tokenEvaluate.result = result
            tokensToBeEvaluated.append(tokenEvaluate)

            if len(openParent) == 0:
                tokenEvaluate.isPrintable = True
                evaluateTokens.append(tokenEvaluate)
        
        # Evaluate Expressiosn
        for tokens in numericExpressions:
            tokenEvaluate: EvaluateToken = EvaluateToken("", "", "")
            result = 0
            pos = 0
            
            while pos < len(tokens):
                token = tokens[pos]
                
                if pos - 1 >= 0 and token.type in acceptedLiterals("binaryOp") and pos + 1 < len(tokens):
                    lastTokenEvaluated = Token(token.type, objToString(result), "", "", "") if result != 0 else tokens[pos - 1]
                    result = evaluateBinaryOperators(token, lastTokenEvaluated, tokens[pos + 1])
                pos += 1
                
            tokenEvaluate.result = result        
            tokenEvaluate.isPrintable = True
            evaluateTokens.append(tokenEvaluate)

    index = 0
    if not isBinaryExpression:
        while index < len(tokens):
            token = tokens[index]
            evaluateToken: EvaluateToken = EvaluateToken(token.type, "", token.line)
            
            if token.type in acceptedLiterals("unaryOp") and index + 1 < len(tokens):
                evaluateToken.result = evaluateUnaryOperators(token, tokens, index)
                evaluateToken.isPrintable = True
                index += 2 if tokens[index + 1].type in acceptedLiterals("unaryOp") else 1
            elif token.type in acceptedLiterals():
                evaluateToken.result = token.lexeme
                evaluateToken.isPrintable = True
            
            evaluateTokens.append(evaluateToken)
            index += 1
    
    return evaluateTokens
        
def getLastEvaluatedToken(evaluateTokens: list[EvaluateToken], leftToken):
    existEvaluate = len(evaluateTokens) != 0 and evaluateTokens[len(evaluateTokens) - 1].result != ""
    result = leftToken
    
    if existEvaluate:
        token = evaluateTokens[len(evaluateTokens) - 1]
        result = Token(token.type, objToString(token.result), "", "", "")
    
    return result