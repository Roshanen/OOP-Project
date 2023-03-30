import time

class Post:
    def __init__(self,u_id,poster,media) -> None:
        self.__id = u_id
        self.__poster = poster
        self.__media_link = media
        self.__rating = Rating()
        self.__comment = []

    def get_info(self):
        info = {
            "id" : self.__id,
            "poster" : self.__poster,
            "media" : self.__media_link,
            "rating" : self.__rating,
            "comment" : self.__comment
        }

        return info

class Rating:
    def __init__(self) -> None:
        self.__thumbs_up_link = ""
        self.__thumbs_down_link = ""
        self.__good_rating = 0
        self.__bad_rating = 0

    def add_rating(self):
        self.__good_rating += 1
    
    def dis_rating(self):
        self.__bad_rating += 1

class Comment:
    def __init__(self,u_id,comment) -> None:
        self.__u_id = u_id
        self.__comment = comment
        self.__date = time.localtime
        self.__replies = []
    
    def reply(self,u_id,reply):
        reply = Comment(u_id,reply)
        self.__replies.append(reply)

class Board:
    def __init__(self,post:list) -> None:
        self.__post = post

    def add_post(self,new_post):
        self.__post.append(new_post)

