from app.classes.evaluate_token import EvaluateToken
from app.classes.token import Token
from app.interpreter.evaluating_exp import evaluate
from app.interpreter.evaluating_exp.converter import objToString
from app.interpreter.scanner import scanner
from app.utility.command_type import CommandType


def sorterMenu(command, file_contents):
    if command == CommandType.TOKENIZE.value:
        tokens: list[Token] = scanner.startScanner(file_contents)
        for token in tokens:
            print(token.msg)
            if token.error: exit(65)
    elif command == CommandType.EVALUATE.value:
        tokens: list[Token] = scanner.startScanner(file_contents)
        del tokens[-1]
        evaluateTokens: list[EvaluateToken] = evaluate.evaluatingExpressions(tokens)
        for token in evaluateTokens:
            if token.result != "" and token.isPrintable:
                print(objToString(token.result))
    elif command == CommandType.PARSE.value:
        return