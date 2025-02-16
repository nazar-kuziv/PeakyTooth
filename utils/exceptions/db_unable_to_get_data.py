class DBUnableToGetData(Exception):
    def __init__(self):
        self.message = "Can't retrieve data from database"
        super().__init__(self.message)