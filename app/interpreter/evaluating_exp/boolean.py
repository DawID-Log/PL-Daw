from app.utility.token_type import TokenType

def isTruthy(value):
    if value == None or value == TokenType.NIL.name.lower(): return False
    if type(convertBoolean(value)) == bool:
        return convertBoolean(value)
    return True

def isEqual(leftOp, rightOp):
    if leftOp == None and rightOp == None: return True
    if leftOp == None: return False
    return convertBoolean(leftOp) == convertBoolean(rightOp)

def convertBoolean(value):
    if value == "true": return True
    elif value == "false": return False
    return None