import sys

from app.constants import CommandName
from app.dummydb import EXISTING_STYLES, get_club
from app.models import Person
from core.command import Command
from core.exceptions import IncorrectCommand
from core.utils import is_integer

CLUB = get_club()


class AddPersonCommand(Command):

    @staticmethod
    def __call__(name, *styles):
        accepted_styles = {}
        name = name.capitalize()

        print('{} пытается пройти фейс-контроль.'.format(name))
        for style in styles:
            checking_style = EXISTING_STYLES.get(style)
            if not checking_style:
                print('Здесь нельзя танцевать "{}"!'.format(style))
                continue
            accepted_styles[style] = checking_style

        if not accepted_styles:
            print('{} пришел сюда только пить.'.format(name))

        person = Person(name=name, styles=accepted_styles)
        CLUB.people.append(person)
        CLUB.update_persons_activities(person)
        print(CLUB)


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

        else:
            playlist_length = 0 if CLUB.playlist_length == 1 else CLUB.playlist_length - 1
            if not is_integer(index, only_positive=True) or int(index) > playlist_length:
                raise IncorrectCommand('В плейлисте нет трека под номером {}'.format(index))
            CLUB.playing = int(index)

        CLUB.update_persons_activities()
        print(CLUB)


class StopCommand(Command):
    @staticmethod
    def __call__(*args):
        CLUB.playing = None
        CLUB.update_persons_activities()
        print(CLUB)


class AddSongCommand(Command):

    @staticmethod
    def __call__(song, *args):
        style = EXISTING_STYLES.get(song)
        if not style:
            raise IncorrectCommand(
                'Композиции в стиле "{}" в нашем клубе не включают.'
                ' У нас предпочитают: {}'.format(
                    song,
                    ', '.join(EXISTING_STYLES.keys()),
            ))

        CLUB.playlist.append(song)
        print('Композиция в стиле: {} добавлена в конец плейлиста'.format(song.capitalize()), CLUB, sep='\n')


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

        CommandName.ADD_PERSON_COMMAND: AddPersonCommand,
    }

    @classmethod
    def get_command(cls, command_name):

        try:
            command = cls.__COMMANDS_MAPPING.get(CommandName(command_name))
        except ValueError:
            raise IncorrectCommand('Не удалось разобрать команду.', command_name)

        return command()
