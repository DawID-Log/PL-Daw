from app.classes.system_argument import SystemArgument
from app.interpreter.menu import sorterMenu
import app.utility.managment_error as managmentError
from app.utility.token_type import TokenType


def main():
    managmentError.checkArgumentNumber()

    systemValue = SystemArgument()
    managmentError.checkCommand(systemValue.command)
    managmentError.checkExtension(systemValue.filename)

    with open(systemValue.filename) as file:
        file_contents = file.read()

    if file_contents:
        sorterMenu(systemValue.command, file_contents)
    else:
        print(TokenType.EOF.value + "  null")


if __name__ == "__main__":
    main()
