import time

class Post:
    def __init__(self,u_id,poster,media) -> None:
        self.__id = u_id
        self.__poster = poster
        self.__media_link = media
        self.__rating = Rating()
        self.__comment = []

class Rating:
    def __init__(self) -> None:
        self.__thumbs_up_link = ""
        self.__thumbs_down_link = ""
        self.__good_rating = 0
        self.__bad_rating = 0

    def add_rating(self):
        pass
    
    def de_rating(self):
        pass

class Comment:
    def __init__(self,u_id,comment) -> None:
        self.__u_id = u_id
        self.__comment = comment
        self.__date = time.localtime
        self.__replies = []
    
    def reply(self,reply):
        pass

class Board:
    def __init__(self,post:list) -> None:
        self.__post = post

    def add_post(self,new_post):
        pass

