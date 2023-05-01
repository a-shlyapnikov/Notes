import view


class User_Interface:
    def __init__(self):
        pass

    def enter(self):
        return input(view.user_input())

    def exit(self):
        view.bye()

    def journal(self, value, revers=False, size=-1):
        view.show_journal(value, revers, size)

    def write_note(self):
        return input(view.title()), input(view.body())


    def write_title(self):
        return input(view.title())


    def write_body(self):
        return input(view.body())


    def add(self):
        view.add()

    def change(self):
        view.change()

    def delete(self):
        view.delete()

    def not_found(self, args):
        view.not_found_command(args[0])
        view.info_info()

    def no_command(self):
        view.no_command()
        view.info_info()

    def no_index(self, num):
        view.no_index(num)

    def fail(self):
        view.fail()

    def choice_number(self):
        return int(input(view.choice_number())) - 1

    def show(self, value):
        view.show_note(value)

    def no_args(self):
        view.no_args()
        view.info_info()


    def no_quotes(self):
        view.no_quotes()

    def error_load(self):
        view.error_load()

    def error_save(self):
        view.error_save()

    def show_info(self):
        view.get_info()