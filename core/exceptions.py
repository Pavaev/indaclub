class IncorrectCommand(Exception):

    def __init__(self, command=None, **extra_kwargs):
        self.command = command
        self.extra_data = extra_kwargs
        super().__init__(command, extra_kwargs)

    def __str__(self):
        return 'Incorrect command: {}'.format(self.command)
