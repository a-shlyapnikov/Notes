class Checker:
    def __init__(self, ui, book):
        self.ui = ui
        self.book = book
        self.revers = False

    def journal(self, args):
        flags = {"-r": self.change_revers,
                 "-d": self.date_sort,
                 "-t": self.title_sort}
        size = -1
        if args[1] != '-r' and args[1].count('r'):
            self.revers = not self.revers
            args[1] = args[1].replace('r', '')
        if len(args) > 2 and args[2].isdigit():
            size = int(args[2])
        try:
            data = flags[args[1]](self.book.get_all_notes())
            self.ui.journal(data, self.revers, size)
            self.revers = not self.revers
        except:
            self.ui.not_found(args[1:])

    def change(self, args):
        num = self.cath_flag(args[:3])
        value = self.cath_double_flag(args[2:])
        return *num, *value

    def change_revers(self, data=''):
        self.revers = True
        return data

    def date_sort(self, items):
        item_dict = {}
        for i in range(len(items)):
            item_dict[items[i].get_change_time()] = items[i]
        return [item_dict[i] for i in sorted(item_dict.keys())]

    def title_sort(self, items):
        item_dict = {}
        for i in range(len(items)):
            item_dict[items[i].get_title()] = items[i]
        return [item_dict[i] for i in sorted(item_dict.keys())]

    def take_value(self, value):
        if value[:1] == '"' and value[-1:] == '"':
            return value[1:-1]
        else:
            self.ui.fail()
            self.ui.no_quotes()

    def take_from_id(self, id):
        items = self.book.get_all_notes()
        return [int(i) for i in range(len(items)) if int(items[i].get_id()) == int(id)]

    def take_from_head(self, head):
        items = self.book.get_all_notes()
        return [int(i) for i in range(len(items)) if items[i].get_head() == head]

    def cath_flag(self, args):
        flags = {"-i": self.take_from_id,
                 "-n": lambda data: [int(data) - 1],
                 "-h": self.take_from_head}
        if len(args) < 3:
            self.ui.no_args()
        elif ((args[1] == '-i' or args[1] == '-n') and args[2].isdigit()) or args[1] == '-h':
            return flags[args[1]](args[2])

    def cath_double_flag(self, args):
        res = {}
        double_flags = {"--title": self.ui.write_title,
                        "--msg": self.ui.write_body}
        catch = [flag for flag in double_flags if flag in args]
        if len(args) != len(catch) * 2 + 1:
            self.ui.no_args()
        elif len(catch):
            for item in catch:
                res[item] = self.take_value(args[args.index(item) + 1])
            for item in [flag for flag in double_flags if flag not in res.keys()]:
                res[item] = double_flags[item]()
            return res['--title'], res['--msg']
    