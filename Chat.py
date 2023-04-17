import datetime


class Chat:
    def __init__(self, owner, members, id):
        self.__id = id
        self.__owner = owner
        self.__message_box = []  # [[text, date, who]]
        self.__members = members

    def send_message(self, message, who):
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        box = [message, date, who]
        self.__message_box.append(box)
        self.update_message()

    def update_message(self):
        for member in self.__members:
            member.add_chat(self)

    def view_message(self):
        return self.__message_box

    def get_id(self):
        return self.__id