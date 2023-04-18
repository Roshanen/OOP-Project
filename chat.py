import datetime


class Chat:
    def __init__(self, owner, members=0, id=0):
        self.__id = id
        self.__owner = owner
        self.__message_box = []  # [[text, date, who]]
        # self.__members = members

    def send_message(self, message, who):
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        box = [message, date, who]
        self.__message_box.append(box)
        self.update_message(box, who)

    def update_message(self, box, who):
        box[2] = self.__owner
        # for member in self.__members:
        #     if member != self.__owner:
        #         member.get_chat().get_message_box().append(box)
            # member.add_chat(self)
        who.get_chat().get_message_box().append(box)

    def get_message_box(self):
        return self.__message_box

    def view_message(self, who):
        display_message = []
        for message in self.__message_box:
            if message[2] == who:
                display_message.append(message)
        return display_message

    def get_id(self):
        return self.__id
