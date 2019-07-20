import sys

from app.constants import CommandName
from app.dummydb import EXISTING_STYLES, get_club
from app.models import Person
from core.command import Command
from core.exceptions import IncorrectCommand
from core.utils import is_integer

CLUB = get_club()


class PlayCommand(Command):
    """Запускает музыку. Принимает номер композиции в плейлсте. Если вызывается
без номера, запускает первую композицию.
    >> /play
    >> /play 5"""

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
    """Останавливает музыку. Все персонажи отправляются в бар."""

    @staticmethod
    def __call__(*args):
        CLUB.playing = None
        CLUB.update_persons_activities()
        print(CLUB)


class AddSongCommand(Command):
    """Добавляет композицию в конец плейлиста, но не запускает ее. Принимает
один из доступных стилей: hip-hop, rnb, electrodance, house, pop.
    >> /addsong hip-hop"""

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
    """Отображает плейлист с номерами композиций"""

    @staticmethod
    def __call__(*args):
        CLUB.show_playlist()


class AddPersonCommand(Command):
    """Добавляет человека в бар. Принимает имя и навыки через пробел
(hip-hop, rnb, electrodance, house, pop) Можно добавить человека без навыков,
указав только имя.
    >> /addperson Василий hip-hop pop
    >> /addperson Никита"""

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


class ExitCommand(Command):
    """Завершает работу клуба. Изменения не будут сохранены."""

    @staticmethod
    def __call__(*args):
        print('Наш клуб закрывается. До свидания!')
        sys.exit()


class StateCommand(Command):
    """Показывает, что происходит в клубе: какая музыка играет и кто что делает."""

    @staticmethod
    def __call__(*args):
        print(CLUB)


class HelpCommand(Command):
    """Список доступных команд с краткой информацией о них. Отображает или все
или же информацию о конкретной команде.
    >> /help
    >> /help /addperson"""

    @staticmethod
    def __call__(command_name=None, *args):
        if command_name:
            command = CommandFactory.get_command(command_name)
            print('{}: {}'.format(command_name, command.__doc__))
            return

        print('Список доступных команд:', end='\n\n')
        for command_name, command in CommandFactory.COMMANDS_MAPPING.items():
            print('{}: {}'.format(command_name.value, command.__doc__), end='\n\n')


class CommandFactory:
    COMMANDS_MAPPING = {
        CommandName.PLAY_COMMAND: PlayCommand,
        CommandName.STOP_COMMAND: StopCommand,
        CommandName.ADD_SONG_COMMAND: AddSongCommand,
        CommandName.PLAYLIST_COMMAND: PlaylistCommand,

        CommandName.ADD_PERSON_COMMAND: AddPersonCommand,

        CommandName.EXIT_COMMAND: ExitCommand,
        CommandName.STATE_COMMAND: StateCommand,
        CommandName.HELP_COMMAND: HelpCommand,
    }

    @classmethod
    def get_command(cls, command_name):

        try:
            command = cls.COMMANDS_MAPPING.get(CommandName(command_name))
        except ValueError:
            raise IncorrectCommand('Не удалось разобрать команду.', command_name)

        return command()
