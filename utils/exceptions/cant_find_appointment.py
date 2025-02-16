class CantFindAppointment(Exception):
    def __init__(self):
        self.message = "Cannot find the appointment"
        super().__init__(self.message)