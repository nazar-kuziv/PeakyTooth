class DBSmthWentWrong(Exception):
    def __init__(self):
        self.message = "Something went wrong while interacting with the database."
        super().__init__(self.message)
