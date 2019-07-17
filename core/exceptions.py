class IncorrectCommand(Exception):

    def __init__(self, message, command=None, **extra_kwargs):
        self.message = message
        self.command = command
        self.extra_data = extra_kwargs
        super().__init__(command, extra_kwargs)

    def __str__(self):
        message = self.message
        if self.command:
            message += ' Команда "{}"'.format(self.command)
        return message
