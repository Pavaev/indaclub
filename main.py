from app.command import CommandFactory
from app.constants import CommandName
from core.exceptions import IncorrectCommand


def main():
    while True:
        command_with_args = input('>> ').strip()
        try:
            command_name, *args = command_with_args.split()
        except ValueError:
            print('Пожалуйста, укажите команду')
            continue

        try:
            command = CommandFactory.get_command(command_name)
        except IncorrectCommand as e:
            print(str(e))
            continue

        try:
            command = CommandFactory.get_command(command_name)
            command(*args)
        except TypeError:
            print('Некорректный вызов команды. Описание: {}'.format(command.__doc__))
            continue
        except IncorrectCommand as e:
            print(str(e))
            continue


if __name__ == '__main__':
    print('Добро пожаловать в наш новый клуб.\n'
          'Введите "/help", если вам нужна помощь.\n'
          'Используйте Ctrl+C или введите "/exit" для выхода из клуба.')
    try:
        main()
    except KeyboardInterrupt:
        CommandFactory.get_command(CommandName.EXIT_COMMAND.value)()
