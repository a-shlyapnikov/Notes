from checker import Checker
from data_base import Data_Base
from ui import User_Interface


class Controller:
    def __init__(self):
        self.run = True
        self.ui = User_Interface()
        self.db = Data_Base(self.ui)
        self.book = self.db.get_book()
        self.checker = Checker(self.ui, self.book)
        self.actions = {'info': self.info,
                        'exit': self.exit,
                        'jr': self.journal,
                        'add': self.add,
                        'del': self.delete,
                        'sh': self.show,
                        'cg': self.change}

    def use(self):
        while(self.run):
            user_entry = self.ui.enter().strip().split()
            try:
                self.actions[user_entry[0]](user_entry)
            except:
                self.not_found([user_entry])

    def journal(self, args):
        if len(args) == 1:
            self.ui.journal(self.book.get_all_notes())
        else:
            self.checker.journal(args)

    def user_friendly(self, func):
        try:
            num = self.ui.choice_number()
            func(num)
        except:
            self.ui.fail()

    def add(self, args):
        if len(args) == 1:
            args = self.ui.write_note()
        else:
            args = self.checker.cath_double_flag(args)
        self.addition(args)

    def addition(self, data):
        try:
            self.book.new(data[0], data[1])
            self.db.save()
            self.ui.add()
        except:
            self.ui.fail()

    def delete(self, args):
        if len(args) == 1:
            self.user_friendly(self.deletion)
        else:
            list(map(self.deletion, [j - i for i, j in enumerate(self.checker.cath_flag(args))]))
        self.db.save()
        self.ui.delete()

    def deletion(self, num):
        if self.book.get_size() > num:
            self.book.delete(num)
        else:
            self.ui.no_index(num)

    def change(self, args):
        if len(args) == 1:
            self.user_friendly(self.entry_change)
        else:
            self.changing(*self.checker.change(args))

    def entry_change(self, num):
        if self.book.get_size() > num:
            title, body = self.ui.write_note()
            self.changing(num, title, body)
        else:
            self.ui.no_index(num)

    def changing(self, num, title, body):
        self.book.change(num, title, body)
        self.db.save()
        self.ui.change()

    def show(self, args):
        if len(args) == 1:
            self.user_friendly(self.showing)
        else:
            list(map(self.showing, [j - i for i, j in enumerate(self.checker.cath_flag(args))]))

    def showing(self, num):
        if self.book.get_size() > num:
            self.ui.show(self.book.get_print(num))
        else:
            self.ui.no_index(num)

    def exit(self, args):
        self.run = False
        self.ui.exit()

    def not_found(self, args):
        self.ui.not_found(args)

    def no_command(self):
        self.ui.no_command()

    def info(self, data=''):
        self.ui.show_info()