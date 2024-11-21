class UserSessionMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class UserSession(metaclass=UserSessionMeta):
    def set_user_data(self, user_id: int, login: str, name: str, surname: str, role: str, organization_id: int,
                      organization_name: int):
        self.user_id = user_id
        self.login = login if login else ''
        self.name = name if name else ''
        self.surname = surname if surname else ''
        self.role = role if role else ''
        self.organization_name = organization_name if organization_name else ''
        self.organization_id = organization_id

    def logout(self):
        self.user_id = None
        self.login = ''
        self.name = ''
        self.surname = ''
        self.role = ''
        self.organization_id = None
        self.organization_name = ''
