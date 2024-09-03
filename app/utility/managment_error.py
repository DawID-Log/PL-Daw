import sys

from app.utility.command_type import CommandType

def checkExtension(filename):
    extension = filename.split(".")[len(filename.split(".")) - 1]
    if extension != "daw" and extension != "lox" :
        print(f"Unknown extension: {extension} try .daw", file=sys.stderr)
        exit(1)

def checkCommand(command):
    if command != CommandType.TOKENIZE.value and command != CommandType.EVALUATE.value and command != CommandType.PARSE.value:
        print(f"Unknown command: {command}", file=sys.stderr)
        exit(1)

def checkArgumentNumber():
    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
        exit(1)

def checkCharEqualErrorToken(char, numberLine, token):
    if char.find(token) > -1:
        print(f"[line {numberLine + 1}] Error: Unexpected character: {char}", file=sys.stderr)
        return True
    return False
    
def checkUnterminatedString(line, numberLine):
    if (line.count("\"") % 2) != 0:
        print(f"[line {numberLine + 1}] Error: Unterminated string.", file=sys.stderr)
        return True