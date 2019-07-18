import sys

from core.command import Command
from app.constants import CommandName, Style
from app.dummydb import get_club
from core.exceptions import IncorrectCommand
from app.models import Person
from core.utils import is_integer

CLUB = get_club()


class AddPersonCommand(Command):

    @staticmethod
    def __call__(name, *args):
        print('{} пытается пройти фейс-контроль'.format(name))
        person = Person(name=name)


class StateCommand(Command):
    @staticmethod
    def __call__(*args):
        print(CLUB)


class ExitCommand(Command):
    @staticmethod
    def __call__(*args):
        print('Наш клуб закрывается. До свидания!')
        sys.exit()


class PlayCommand(Command):
    @staticmethod
    def __call__(index=None, *args):
        if not CLUB.playlist:
            raise IncorrectCommand('Плейлист пуст.')

        if index is None:
            CLUB.playing = 0
            # сейчас играет
            print(CLUB)
            return

        playlist_length = 0 if CLUB.playlist_length == 1 else CLUB.playlist_length - 1
        if not is_integer(index, only_positive=True) or int(index) > playlist_length:
            raise IncorrectCommand('В плейлисте нет трека под номером {}'.format(index))

        CLUB.playing = int(index)
        # update persons
        print(CLUB)


class StopCommand(Command):
    @staticmethod
    def __call__(*args):
        CLUB.playing = None
        print(CLUB)
        # update persons


class AddSongCommand(Command):

    @staticmethod
    def __call__(song, *args):

        try:
            style = Style(song.lower())
        except ValueError:
            raise IncorrectCommand(
                'Композиции в стиле {} в нашем клубе не слушают.'
                ' У нас предпочитают: {}'.format(
                    song,
                    ', '.join(map(lambda x: x.value.capitalize(), Style)),
            ))

        CLUB.playlist.append(style)
        print('Композиция в стиле: {} добавлена в конец плейлиста'.format(song.capitalize()), CLUB, sep='\n')
        # сейчас играет


class PlaylistCommand(Command):

    @staticmethod
    def __call__(*args):
        CLUB.show_playlist()


class CommandFactory:
    __COMMANDS_MAPPING = {
        CommandName.EXIT_COMMAND: ExitCommand,
        CommandName.STATE_COMMAND: StateCommand,
        CommandName.PLAY_COMMAND: PlayCommand,
        CommandName.ADD_SONG_COMMAND: AddSongCommand,
        CommandName.PLAYLIST_COMMAND: PlaylistCommand,
        CommandName.STOP_COMMAND: StopCommand,
    }

    @classmethod
    def get_command(cls, command_name):

        try:
            command = cls.__COMMANDS_MAPPING.get(CommandName(command_name))
        except ValueError:
            raise IncorrectCommand('Не удалось разобрать команду.', command_name)

        return command()
