class User:
    
    user = []

    def __init__(self, name, password):
        self.name = name
        self.password = password
        User.user = {"name": self.name, "password": self.password}
    
    @classmethod
    def return_user(cls):
        return cls.user