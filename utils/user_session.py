class UserSessionMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class UserSession(metaclass=UserSessionMeta):
    def set_user_data(self, login: str, name: str, surname: str, role: str, organization: str):
        self.login = login if login else ''
        self.name = name if name else ''
        self.surname = surname if surname else ''
        self.role = role if role else ''
        self.organization = organization if organization else ''
