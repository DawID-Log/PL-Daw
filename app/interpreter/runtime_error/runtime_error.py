from contextvars import Token

class RuntimeError(RuntimeError):
    token: Token
    
    def __init__(self, token: Token, msg: str):
        super(msg)
        self.token = token