import sys

from core.command import SimpleCommand, Command
from core.constants import CommandName
from core.dummydb import Club, get_db
from core.exceptions import IncorrectCommand


_CLUB = Club()


class AddUserCommand(Command):

    @classmethod
    def __call__(cls):
        db = get_db()
        db.person_list.append('xxx')


class StateCommand(SimpleCommand):
    @classmethod
    def __call__(cls):
        db = get_db()
        print(db.person_list)


class ExitCommand(SimpleCommand):
    @classmethod
    def __call__(cls):
        print('Our club is close. Bye!')
        sys.exit()


class CommandFactory:
    __COMMANDS_MAPPING = {
        CommandName.EXIT_COMMAND.value: ExitCommand,
        CommandName.STATE_COMMAND.value: StateCommand,
        CommandName.ADD_USER_COMMAND.value: AddUserCommand,
    }

    @classmethod
    def get_command(cls, command_name):
        command = cls.__COMMANDS_MAPPING.get(command_name)
        if not command:
            raise IncorrectCommand(command_name)
        return command()
