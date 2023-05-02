import datetime


class Chat:
    def __init__(self, user):
        self.__message_box = []
        self.__owner = user
        # [{"text":text, "date":date, "who":who}, {"text":text, "date":date, "who":who}, ...]

    def send_message(self, message, who, sender):
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        box = {'text': message, 'date': date, 'who': who, 'sender': sender}
        self.__message_box.append(box)
        self.update_message(message, date, who)

    def update_message(self, message, date, who):
        new_box = {'text': message, 'date': date, 'who': self.__owner, 'sender': self.__owner}
        who.get_chat().get_message_box().append(new_box)

    def get_message_box(self):
        return self.__message_box

    def view_message(self, who):
        display_message = []
        for message in self.__message_box:
            if message['who'] == who:
                display_message.append(message)
        return display_message
