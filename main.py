from app.command import CommandFactory
from core.constants import CommandName
from core.exceptions import IncorrectCommand


def main():
    while True:
        command_name = input('>>> ')

        try:
            command = CommandFactory.get_command(command_name)
        except IncorrectCommand as e:
            print(str(e))
            continue

        if command:
            command()


if __name__ == '__main__':
    try:
        print('Welcome to our new club.\n'
              'Type "/help", if you need help.\n'
              'Use Ctrl+C or type "/exit" for exit, as you probably guessed =)')
        main()
    except KeyboardInterrupt:
        CommandFactory.get_command(CommandName.EXIT_COMMAND.value)()
