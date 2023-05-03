import datetime
from utilities import IdGenerator


class Community:
    def __init__(self):
        self.__boards = []

    def add_board(self, *args):
        for board in args:
            self.__boards.append(board)

    def get_board(self, board_name):
        for board in self.__boards:
            if board.get_name() == board_name:
                return board

        return None


class Post:
    def __init__(self,poster, media, game_name):
        self.__id = IdGenerator.generate_id(id(self))
        self.__poster = poster
        self.__media_link = media
        self.__rating = Rating()
        self.__game_name = game_name
        self.__comment = []
        self.__like_user = []

    def get_game_name(self):
        return self.__game_name

    def get_media(self):
        return self.__media_link

    def get_rating(self):
        return self.__rating.get_rating()

    def get_poster(self):
        return self.__poster

    def get_comment_number(self):
        return len(self.__comment)

    def get_id(self):
        return self.__id

    def rate_up(self, user):
        if user not in self.__like_user:
            self.__like_user.append(user)
            self.__rating.add_rating()
        else:
            self.__like_user.remove(user)
            self.__rating.minus_rating()

class Rating:
    def __init__(self) -> None:
        self.__thumbs_up_pic = ""
        self.__thumbs_down_pic = ""
        self.__good_rating = 0
        self.__bad_rating = 0

    def get_rating(self):
        return self.__good_rating

    def add_rating(self):
        self.__good_rating += 1

    def minus_rating(self):
        self.__good_rating -= 1

    def dis_rating(self):
        self.__bad_rating += 1


class Comment:
    def __init__(self,comment) -> None:
        self.__comment = comment
        self.__date = datetime.datetime.now()
        self.__replies = []
    
    def reply(self,reply):
        reply = Comment(reply)
        self.__replies.append(reply)

    def get_comment(self):
        return self.__comment

    def get_replies(self):
        return self.__replies


class Board:
    def __init__(self, name):
        self.__name = name
        self.__post = []

    def add_post(self,new_post):
        self.__post.append(new_post)

    def get_all_post(self):
        return self.__post

    def get_post(self, post_id):
        post = None
        for each_post in self.__post:
            if each_post.get_id() == post_id:
                post = each_post
                break

        return post

    def get_name(self):
        return self.__name

    def __repr__(self):
        return self.__name