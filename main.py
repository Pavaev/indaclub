from app.command import CommandFactory
from core.constants import CommandName
from core.exceptions import IncorrectCommand


def main():
    while True:
        command_with_args = input('>> ').strip()
        command_name, *args = command_with_args.split(' ')

        try:
            command = CommandFactory.get_command(command_name)
            command(*args)
        except IncorrectCommand as e:
            print(str(e))
            continue


if __name__ == '__main__':
    print('Добро пожаловать в наш новый клуб.\n'
          'Введите "/help", если вам нужна помощь.\n'
          'Используйте Ctrl+C или введите "/exit" для выхода из клуба')
    try:
        main()
    except KeyboardInterrupt:
        CommandFactory.get_command(CommandName.EXIT_COMMAND.value)()
