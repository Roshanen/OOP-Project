import time
from WebSystem import *

class Post:
    def __init__(self,poster,media):
        self.__poster = poster
        self.__media_link = media
        self.__rating = Rating()
        self.__comment = []

    def get_info(self):
        info = {
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

    def get_rating(self):
        return self.__bad_rating,self.__good_rating

    def add_rating(self):
        self.__good_rating += 1
    
    def dis_rating(self):
        self.__bad_rating += 1

class Comment:
    def __init__(self,comment) -> None:
        self.__comment = comment
        self.__date = time.localtime
        self.__replies = []
    
    def reply(self,reply):
        reply = Comment(reply)
        self.__replies.append(reply)

    def get_comment(self):
        return self.__comment

    def get_replies(self):
        return self.__replies

class Board:
    def __init__(self,post:list) -> None:
        self.__post = post

    def add_post(self,new_post):
        self.__post.append(new_post)

    def get_post(self):
        return self.__post