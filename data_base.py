from book import Book
import os


class Data_Base:
    def __init__(self, ui):
        self.book = Book()
        self.ui = ui

    def get_book(self):
        self.load()
        return self.book

    def load(self):
        try:
            with open('notes_db.json', 'r') as file:
                data = file.read().split('"book": [')
                count = int(data[0].replace('\n', '').replace(' ', '')
                            .replace(',', '').replace('{"count":', ''))
                self.book.set_count(count)
                items = data[1].replace(']\n}', '').replace(']}', '').replace('{', '')
                items = items[:items.rfind('}')].split('},')
            for item in items:
                id, title, body, create_time, last_change = self.parse(item)
                self.board.load(id, title, body, create_time, last_change)
        except:
            if os.path.isfile('notes_db.json'):
                self.ui.error_load()

    def save(self):
        try:
            with open('notes_db.json', 'w') as file:
                data = '{"count": %d, "board": [' % (self.book.get_count())
                for item in self.book.get_all_notes():
                    data += '{' + item.get_data() + '},'
                file.write(data[:-1] + ']}')
        except:
            self.ui.error_save()

    def parse(self, value):
        id = value[6:value.index(', "title":')]
        title = value[value.index('"title": ') + 9:value.index('", "body":')]
        body = value[value.index('"body": ') + 9:value.index('", "create_time":')]
        create_time = value[value.index('"create_time": ') + 16:value.index('", "last_change":')]
        last_change = value[value.index('"last_change": ') + 16:-1]
        return id, title, body, create_time, last_change