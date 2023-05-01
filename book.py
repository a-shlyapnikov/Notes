from note import Note

class Book:
    def __init__(self):
        self.notes = []
        self.count = 0    

    def __str__(self):
        view = ''
        for item in self.notes:
            view += item + '\n\n'
        return view
    
    def set_count(self, value):
        self.count = value
    
    def new(self, title, body):
        self.notes.append(Note(self.count, title, body))
        self.count += 1

    def load(self, id, title, body, create_time, last_change):
        self.notes.append(Note(id, title, body, create_time, last_change))

    def change(self, num, title, body):
        self.notes[num].set_note(title, body)
    
    def delete(self, num):
        self.notes.pop(num)

    def get_note(self, index):
        return self.notes[index].get_note()

    def get_all_notes(self):
        return self.notes


    def get_count(self):
        return self.count

    def get_size(self):
        return len(self.notes)

    def get_print(self, index):
        return self.notes[index]

    def get_data_change(self, index):
        return self.notes[index].get_change_time()

