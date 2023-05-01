from datetime import *

class Note:
    def __init__(self, id, title, body, create_time ='', last_change=''):
        self._id = id
        self._title = title
        self._body = body
        if create_time == '':
            self._create_time = datetime.now().strftime("Y-%m-%d %H:%M:%S")
        else:
            self._create_time = create_time
        if last_change == '':
            self._last_change = datetime.now().strftime("Y-%m-%d %H:%M:%S")
        else:
            self._last_change = last_change
    
    def __str__(self):
        id = '000'[:-len(str(self._id))] + str(self._id)
        return f'{id}.\t{self._title}\n\n{self._body}\n\n' \
               f'Создано: {self._create_time}\nПоследнее изменение:{self._last_change}'
    
    def set_title(self, new_title):
        self._title = new_title
        self._last_change = datetime.now().strftime("Y-%m-%d %H:%M:%S")
    
    def set_body(self, new_body):
        self._body = new_body
        self._last_change = datetime.now().strftime("Y-%m-%d %H:%M:%S")

    def set_note(self, new_title, new_body):
        self.set_title(new_title)
        self.set_body(new_body)
    
    def get_note(self):
        return {"id": self._id, "title": self._title, "body": self._body,
                "create_time": self._create_time, "last_change": self._last_change}
    
    def get_id(self):
        return self._id
    
    def get_title(self):
        return self._title

    def get_body(self):
        return self._body
    
    def get_create_time(self):
        return self._create_time

    def get_change_time(self):
        return self._last_change

    def get_journal_data(self):
        return self._id, self._title, self._last_change

    def get_data(self):
        return f'"id": {self._id}, "title": "{self._title}", "body": "{self._body}", ' \
               f'"create_time": "{self._create_time}", "last_change": "{self._last_change}"'
        

        