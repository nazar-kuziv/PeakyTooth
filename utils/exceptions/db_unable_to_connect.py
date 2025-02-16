class DBUnableToConnect(Exception):
    def __init__(self):
        self.message = 'Unable to connect to database'
        super().__init__(self.message)