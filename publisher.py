from user import User


class Publisher(User):
    def __init__(self, system, name, password, game_owned, profile_picture=None, description=None, level=0):
        super().__init__(system, name, password, profile_picture, description, level)
        self.__game_owned = []
