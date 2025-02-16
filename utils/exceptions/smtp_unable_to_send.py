class SMTPUnableToSend(Exception):
    def __init__(self):
        self.message = 'Unable to send message'
        super().__init__(self.message)
