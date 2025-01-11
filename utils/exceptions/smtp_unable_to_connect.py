class SMTPUnableToConnect(Exception):
    def __init__(self):
        self.message = 'Unable to connect to the email server'
        super().__init__(self.message)
