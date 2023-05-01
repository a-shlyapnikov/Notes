import view
from controller import Controller

class Presenter:
    def __init__(self, args):
        self.args = args
        self.controller = Controller()
        self.function = {'info': self.controller.info,
                         'add': self.controller.add,
                         'del': self.controller.delete,
                         'sh': self.controller.show,
                         'jr': self.controller.journal,
                         'cg': self.controller.change}


    def start(self):
        try:
            self.test_quotes()
            self.function[self.args[1]](self.args[1:])
        except:
            if len(self.args) == 1:
                self.controller.use()
            else:
                self.controller.not_found(self.args[1:])

    def test_quotes(self):
        flags = ["--title", "--msg"]
        for flag in flags:
            if self.args.count(flag ):
                self.args[self.args.index(flag) + 1] = '"' + self.args[self.args.index(flag) + 1] + '"'