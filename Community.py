import time

class Post:
    def __init__(self,u_id,poster,media) -> None:
        self.id = u_id
        self.poster = poster
        self.media_link = media
        self.rating = Rating()
        self.comment = []

class Rating:
    def __init__(self) -> None:
        self.thumbs_up_link = ""
        self.thumbs_down_link = ""
        self.good_rating = 0
        self.bad_rating = 0

    def add_rating(self):
        pass
    
    def de_rating(self):
        pass

class Comment:
    def __init__(self,u_id,comment) -> None:
        self.u_id = u_id
        self.comment = comment
        self.date = time.localtime
        self.replies = []
    
    def reply(self,reply):
        pass

class Board:
    def __init__(self,post:list) -> None:
        self.post = post

    def add_post(self,new_post):
        pass

