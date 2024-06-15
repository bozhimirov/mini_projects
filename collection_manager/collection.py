from tkinter import *
from tkinter import ttk


class ModelDB:
    def __init__(self):
        self.file_list = {
            'Movies': 'movies.csv',
            'Games': 'games.csv',
            'Books': 'books.csv',
        }

    def get_all_from_file(self, a_frame):
        try:
            with open(self.file_list[a_frame], 'r') as f:
                all_list = f.readlines()
                list_o = []
                for el in all_list:
                    if el != '\n':
                        new_l = el[:-1]
                        list_o.append(new_l)
                return list_o
        except FileNotFoundError:
            return []

    @staticmethod
    def add_to_file_dummy(data):
        frame = data[0]
        n_data = ''
        if frame == 'Movies':
            n, y, g, d, a = data[1], data[2], data[3], data[4], data[5]
            n_data = f"'{n}', '{y}', '{g}', '{d}', '{a}'"
        elif frame == 'Games':
            n, y, g, o = data[1], data[2], data[3], data[4]
            n_data = f"'{n}', '{y}', '{g}', '{o}'"
        elif frame == 'Books':
            n, y, g, a = data[1], data[2], data[3], data[4]
            n_data = f"'{n}', '{y}', '{g}', '{a}'"
        return frame, n_data

    def add_to_file(self, data):
        frame, n_data = self.add_to_file_dummy(data)

        try:
            with open(self.file_list[frame], 'a') as f:
                f.write(n_data + '\n')
        except FileNotFoundError:
            with open(self.file_list[frame], 'x') as f:
                f.write(n_data + '\n')

    def replace_from_file(self, old_data, new_data):
        if new_data != '':
            _, nn_data = self.add_to_file_dummy(new_data)
        else:
            nn_data = '\n'
        frame, n_data = self.add_to_file_dummy(old_data)

        try:
            handle = open(self.file_list[frame], 'r')
            content = handle.read()
            content = content.replace(n_data, nn_data)
            handle.close()
            handle = open(self.file_list[frame], 'w')
            handle.write(content)
            handle.close()
        except FileNotFoundError:
            return []


class BaseItem:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre


class Movie(BaseItem):
    def __init__(self, title, year, genre, director, actors):
        super().__init__(title, year, genre)
        self.director = director
        self.actors = actors

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title, self.year, self.genre, self.director, self.actors


class Game(BaseItem):
    def __init__(self, title, year, genre, owner):
        super().__init__(title, year, genre)
        self.owner = owner

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title, self.year, self.genre, self.owner


class Book(BaseItem):
    def __init__(self, title, year, genre, author):
        super().__init__(title, year, genre)
        self.author = author

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title, self.year, self.genre, self.author


class Collection:

    def __init__(self):
        self.collection = {
            'Movies': [],
            'Games': [],
            'Books': [],
        }

    def __str__(self):
        data = []
        for k, v in self.collection.items():
            ls = []
            for val in v:
                ls.append(str(val))
            data.append(f'{k}: {",".join(ls)}')

        return f'{",".join(data)}'

    @staticmethod
    def make_movie_item(args):
        t, y, g, d, a = args[0][1:-1], args[1][1:-1], args[2][1:-1], args[3][1:-1], args[4][1:-1]
        item = Movie(t, y, g, d, a)
        return item

    @staticmethod
    def make_game_item(args):
        t, y, g, o = args[0][1:-1], args[1][1:-1], args[2][1:-1], args[3][1:-1]
        item = Game(t, y, g, o)
        return item

    @staticmethod
    def make_book_item(args):
        t, y, g, a = args[0][1:-1], args[1][1:-1], args[2][1:-1], args[3][1:-1]
        item = Book(t, y, g, a)
        return item

    def clear_from_collection(self, frame):
        self.collection[frame] = []

    def add_to_collection(self, frame, args):
        args = args.split(', ')
        item = ''
        if frame == "Movies":
            item = self.make_movie_item(args)
            if item not in self.collection[frame]:
                self.collection[frame].append(item)

        elif frame == "Games":
            item = self.make_game_item(args)
            if item not in self.collection[frame]:
                self.collection[frame].append(item)
        elif frame == "Books":
            item = self.make_book_item(args)

            if item not in self.collection[frame]:
                self.collection[frame].append(item)
        return item

    def get_data_from_collection_item(self, frame, name):
        data = []
        if frame == 'Movies':
            for item in self.collection[frame]:
                if item.title == name:
                    data.append(item.title)
                    data.append(item.year)
                    data.append(item.genre)
                    data.append(item.director)
                    data.append(item.actors)
                    break
        elif frame == 'Games':
            for item in self.collection[frame]:
                if item.title == name:
                    data.append(item.title)
                    data.append(item.year)
                    data.append(item.genre)
                    data.append(item.owner)
                    break
        elif frame == 'Books':
            for item in self.collection[frame]:
                if item.title == name:
                    data.append(item.title)
                    data.append(item.year)
                    data.append(item.genre)
                    data.append(item.author)
                    break
        return data

    def show_item_from_collection(self, frame, name):
        if frame == 'Movies':
            for item in self.collection[frame]:
                if item.title == name:
                    return item
        elif frame == 'Games':
            for item in self.collection[frame]:
                if item.title == name:
                    return item
        elif frame == 'Books':
            for item in self.collection[frame]:
                if item.title == name:
                    return item


class View(Tk):
    MENU_TITLES = [
        'Movies', 'Games', 'Books'
    ]
    ACTIVE = MENU_TITLES[0]
    MAIN_FRAMES = {}

    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.title('Collection Manager')
        self.menubar = Menu(self)
        self.entry_fields = {}
        self._create_main_window()
        self._make_menubar()
        self.active_frame = self.ACTIVE
        self.controller.make_data_to_item_to_collection(self.ACTIVE)
        self.data = []

    def main(self):
        self.mainloop()

    def _make_menubar(self):
        for name in self.MENU_TITLES:
            self.menubar.add_command(label=name, command=lambda menu=name: self.controller.listen_menu_tab_state(menu))
            if name == self.ACTIVE:
                self.menubar.entryconfig(name, state='disabled')
                self.MAIN_FRAMES[self.ACTIVE].grid(column=0, row=0)
        self.config(menu=self.menubar)

    def set_choices(self, value):
        self.l_box.delete(0, END)

        for c in value:
            self.l_box.insert(END, c)

    def _create_main_window(self):
        self.geometry = '300x300'
        for i in range(len(self.MENU_TITLES)):
            self.MAIN_FRAMES[self.MENU_TITLES[i]] = ttk.Frame(self)
            some_name_box = ttk.Label(self.MAIN_FRAMES[self.MENU_TITLES[i]],
                                      text=f'Collection Manager {self.MENU_TITLES[i]}', font=('bold', 12), padding=5)
            some_name_box.grid(column=0, columnspan=2, row=1, padx=20, pady=20)

            search_button = ttk.Button(self.MAIN_FRAMES[self.MENU_TITLES[i]], text=f'Search {self.MENU_TITLES[i]}',
                                       command=lambda action='search': self.controller.action_buttons(action), width=15)
            search_button.grid(column=4, row=1, sticky='ewn')

            result_box = ttk.Frame(self.MAIN_FRAMES[self.MENU_TITLES[i]])
            result_box.grid(column=0, columnspan=5, row=2, rowspan=5, sticky='news')

            collection_box = ttk.Frame(result_box)
            collection_box.grid(column=0, row=0, rowspan=4, sticky='news')

            choices = []

            choicevar = StringVar(self, value=choices, name='choicev')
            self.l_box = Listbox(collection_box, height=5, listvariable=choicevar, selectmode='browse')
            self.l_box.grid(column=0, row=0, sticky='news')
            self.l_box.bind('<<ListboxSelect>>', self.selected_item_str)
            s = ttk.Scrollbar(collection_box, orient=VERTICAL, command=self.l_box.yview)
            s.grid(column=0, row=0, rowspan=6, sticky='ens')
            self.l_box['yscrollcommand'] = s.set

            details_box = ttk.Labelframe(result_box, text='Main Info', width=100, height=160)
            details_box.grid(column=1, row=0, rowspan=4, sticky='news')

            btn_box = ttk.Frame(result_box, padding=(0, 1, 0, 0))
            btn_box.grid(column=4, row=0, rowspan=5, sticky='news', pady=15)
            if self.MENU_TITLES[i] == 'Movies':
                self.add_btn_m = ttk.Button(btn_box, text='add',
                                            command=lambda action='add': self.controller.action_buttons(action))
                self.add_btn_m.grid(column=0, row=1, sticky='news')
                self.m_search_box = ttk.Entry(self.MAIN_FRAMES[self.MENU_TITLES[i]], width=20)
                self.m_search_box.grid(column=3, row=1, sticky='ewn')
                self.m_name_entry = ttk.Entry(details_box)
                self.m_name_entry.grid(column=1, row=0, sticky='w')
                self.m_year_entry = ttk.Entry(details_box)
                self.m_year_entry.grid(column=1, row=1, sticky='w')
                self.m_genre_entry = ttk.Entry(details_box)
                self.m_genre_entry.grid(column=1, row=2, sticky='w')
                self.m_director_entry = ttk.Entry(details_box)
                self.m_director_entry.grid(column=1, row=3, sticky='w')
                self.m_actor_entry = ttk.Entry(details_box)
                self.m_actor_entry.grid(column=1, row=4, sticky='w')
                self.generate_common_labels(details_box)
                director_label = ttk.Label(details_box, text='Director:', width=20)
                director_label.grid(column=0, row=3, sticky='e')
                actor_label = ttk.Label(details_box, text='Main Actor:', width=20)
                actor_label.grid(column=0, row=4, sticky='e')

            elif self.MENU_TITLES[i] == 'Games':
                self.add_btn_g = ttk.Button(btn_box, text='add',
                                            command=lambda action='add': self.controller.action_buttons(action))
                self.add_btn_g.grid(column=0, row=1, sticky='news')
                self.g_search_box = ttk.Entry(self.MAIN_FRAMES[self.MENU_TITLES[i]], width=20)
                self.g_search_box.grid(column=3, row=1, sticky='ewn')
                self.g_name_entry = ttk.Entry(details_box)
                self.g_name_entry.grid(column=1, row=0, sticky='w')
                self.g_year_entry = ttk.Entry(details_box)
                self.g_year_entry.grid(column=1, row=1, sticky='w')
                self.g_genre_entry = ttk.Entry(details_box)
                self.g_genre_entry.grid(column=1, row=2, sticky='w')
                self.g_owner_entry = ttk.Entry(details_box)
                self.g_owner_entry.grid(column=1, row=3, sticky='w')
                self.generate_common_labels(details_box)
                owner_label = ttk.Label(details_box, text='Owner:', width=20)
                owner_label.grid(column=0, row=3, sticky='e')
            elif self.MENU_TITLES[i] == 'Books':
                self.add_btn_b = ttk.Button(btn_box, text='add',
                                            command=lambda action='add': self.controller.action_buttons(action))
                self.add_btn_b.grid(column=0, row=1, sticky='news')
                self.b_search_box = ttk.Entry(self.MAIN_FRAMES[self.MENU_TITLES[i]], width=20)
                self.b_search_box.grid(column=3, row=1, sticky='ewn')
                self.b_name_entry = ttk.Entry(details_box)
                self.b_name_entry.grid(column=1, row=0, sticky='w')
                self.b_year_entry = ttk.Entry(details_box)
                self.b_year_entry.grid(column=1, row=1, sticky='w')
                self.b_genre_entry = ttk.Entry(details_box)
                self.b_genre_entry.grid(column=1, row=2, sticky='w')
                self.b_author_entry = ttk.Entry(details_box)
                self.b_author_entry.grid(column=1, row=3, sticky='w')
                self.generate_common_labels(details_box)
                author_label = ttk.Label(details_box, text='Author:', width=20)
                author_label.grid(column=0, row=3, sticky='e')

            self.update_btn = ttk.Button(btn_box, text='update',
                                         command=lambda action='update': self.controller.action_buttons(action))
            self.update_btn.grid(column=0, row=2, sticky='news')
            self.remove_btn = ttk.Button(btn_box, text='remove',
                                         command=lambda action='remove': self.controller.action_buttons(action))
            self.remove_btn.grid(column=0, row=3, sticky='news')
            self.clear_btn = ttk.Button(btn_box, text='clear',
                                        command=lambda action='clear': self.controller.action_buttons(action))
            self.clear_btn.grid(column=0, row=4, sticky='news')

    @staticmethod
    def generate_common_labels(details_box):
        name_label = ttk.Label(details_box, text='Name:', width=20)
        name_label.grid(column=0, row=0, sticky='e')
        year_label = ttk.Label(details_box, text='Year:', width=20)
        year_label.grid(column=0, row=1, sticky='e')
        genre_label = ttk.Label(details_box, text='Genre:', width=20)
        genre_label.grid(column=0, row=2, sticky='e')

    def selected_item_str(self, a):
        if a.widget.curselection() not in [(), '']:
            selected_item = self.l_box.get(a.widget.curselection())
            try:
                data = self.controller.search_item(self.active_frame, selected_item)
                self.data = data
            except AttributeError:
                pass
            self.set_entries(data)
        self.add_btn_m['state'] = 'disabled'
        self.add_btn_g['state'] = 'disabled'
        self.add_btn_b['state'] = 'disabled'
        self.update()

    def get_searched(self):
        if self.active_frame == "Movies":
            s = self.m_search_box.get()
            return s
        elif self.active_frame == "Games":
            s = self.g_search_box.get()
            return s
        elif self.active_frame == "Books":
            s = self.b_search_box.get()
            return s

    def get_entries(self):
        if self.active_frame == "Movies":
            n = self.m_name_entry.get()
            y = self.m_year_entry.get()
            g = self.m_genre_entry.get()
            d = self.m_director_entry.get()
            a = self.m_actor_entry.get()
            if n == '' or y == '' or g == '' or d == '' or a == '':
                return ''
            return self.active_frame, n, y, g, d, a
        elif self.active_frame == "Games":
            n = self.g_name_entry.get()
            y = self.g_year_entry.get()
            g = self.g_genre_entry.get()
            o = self.g_owner_entry.get()
            if n == '' or y == '' or g == '' or o == '':
                return ''
            return self.active_frame, n, y, g, o
        elif self.active_frame == "Books":
            n = self.b_name_entry.get()
            y = self.b_year_entry.get()
            g = self.b_genre_entry.get()
            a = self.b_author_entry.get()
            if n == '' or y == '' or g == '' or a == '':
                return ''
            return self.active_frame, n, y, g, a

    def set_entries(self, dataset):
        if self.active_frame == "Movies":
            n, y, g, d, a = dataset
            self.m_name_entry.delete(0, END)
            self.m_name_entry.insert(0, n)
            self.m_year_entry.delete(0, END)
            self.m_year_entry.insert(0, y)
            self.m_genre_entry.delete(0, END)
            self.m_genre_entry.insert(0, g)
            self.m_director_entry.delete(0, END)
            self.m_director_entry.insert(0, d)
            self.m_actor_entry.delete(0, END)
            self.m_actor_entry.insert(0, a)
        elif self.active_frame == "Games":
            n, y, g, o = dataset
            self.g_name_entry.delete(0, END)
            self.g_name_entry.insert(0, n)
            self.g_year_entry.delete(0, END)
            self.g_year_entry.insert(0, y)
            self.g_genre_entry.delete(0, END)
            self.g_genre_entry.insert(0, g)
            self.g_owner_entry.delete(0, END)
            self.g_owner_entry.insert(0, o)
        elif self.active_frame == "Books":
            n, y, g, a = dataset
            self.b_name_entry.delete(0, END)
            self.b_name_entry.insert(0, n)
            self.b_year_entry.delete(0, END)
            self.b_year_entry.insert(0, y)
            self.b_genre_entry.delete(0, END)
            self.b_genre_entry.insert(0, g)
            self.b_author_entry.delete(0, END)
            self.b_author_entry.insert(0, a)

    def clear_entries(self):
        if self.active_frame == "Movies":
            self.m_search_box.delete(0, 'end')
            self.m_name_entry.delete(0, 'end')
            self.m_year_entry.delete(0, 'end')
            self.m_genre_entry.delete(0, 'end')
            self.m_director_entry.delete(0, 'end')
            self.m_actor_entry.delete(0, 'end')
        elif self.active_frame == "Games":
            self.g_search_box.delete(0, 'end')
            self.g_name_entry.delete(0, 'end')
            self.g_year_entry.delete(0, 'end')
            self.g_genre_entry.delete(0, 'end')
            self.g_owner_entry.delete(0, 'end')
        elif self.active_frame == "Books":
            self.b_search_box.delete(0, 'end')
            self.b_name_entry.delete(0, 'end')
            self.b_year_entry.delete(0, 'end')
            self.b_genre_entry.delete(0, 'end')
            self.b_author_entry.delete(0, 'end')
        self.add_btn_m['state'] = 'active'
        self.add_btn_g['state'] = 'active'
        self.add_btn_b['state'] = 'active'
        self.update()


class Controller:
    def __init__(self):
        self.collection = Collection()
        self.model = ModelDB()
        self.view = View(self)
        self.active_frame = "Movies"
        self.make_initial_choices()

    def main(self):
        self.view.main()

    def listen_menu_tab_state(self, frame):
        for name in self.view.MENU_TITLES:
            if name == frame:
                self.view.active_frame = name
                self.make_data_to_item_wo_add_to_collection(frame)
                self.make_data_to_item_to_collection(frame)
                self.view.menubar.entryconfig(name, state='disabled')
                self.view.MAIN_FRAMES[name].grid(column=0, row=0)
                self.active_frame = frame
                self.make_initial_choices()
                self.view.clear_entries()

            else:
                self.view.menubar.entryconfig(name, state='normal')
                self.view.MAIN_FRAMES[name].grid_forget()

    def make_initial_choices(self):
        var = self.make_data_to_item_wo_add_to_collection(self.active_frame)
        self.view.set_choices(var)

    def get_all_data_from_db(self, frame):
        db_data = self.model.get_all_from_file(frame)
        return db_data

    def clear_data_from_collection(self, frame):
        self.collection.clear_from_collection(frame)

    def make_data_to_item_to_collection(self, frame):
        self.clear_data_from_collection(frame)
        db_data = self.get_all_data_from_db(frame)
        for line in db_data:
            self.collection.add_to_collection(frame, line)

    def make_data_to_item_wo_add_to_collection(self, frame):
        db_data = self.get_all_data_from_db(frame)
        choices = []
        for line in db_data:
            item = ''
            args = line.split(', ')
            if frame == "Movies":
                item = self.collection.make_movie_item(args)
            elif frame == "Games":
                item = self.collection.make_game_item(args)
            elif frame == "Books":
                item = self.collection.make_book_item(args)
            choices.append(item.title)
        return choices

    def search_item(self, frame, name):
        data = self.collection.get_data_from_collection_item(frame, name)
        return data

    def action_buttons(self, action):
        data = self.view.get_entries()
        old_data = [self.active_frame] + self.view.data
        if data != '':
            if action == 'add':
                self.model.add_to_file(data)
                self.view.clear_entries()
                self.make_initial_choices()
                self.make_data_to_item_to_collection(self.active_frame)
            elif action == 'update':
                self.model.replace_from_file(old_data, data)
                self.view.clear_entries()
                self.make_data_to_item_wo_add_to_collection(self.active_frame)
                self.make_data_to_item_to_collection(self.active_frame)
                self.make_initial_choices()
            elif action == 'remove':
                self.model.replace_from_file(old_data, '')
                self.view.clear_entries()
                self.make_data_to_item_wo_add_to_collection(self.active_frame)
                self.make_data_to_item_to_collection(self.active_frame)
                self.make_initial_choices()

        if action == 'clear':
            self.view.clear_entries()
        elif action == 'search':
            name = self.view.get_searched()
            if name != '':
                item = self.collection.show_item_from_collection(self.active_frame, name)
                var = [item]
                self.view.set_choices(var)
                self.view.update()
            else:
                self.make_initial_choices()


if __name__ == '__main__':
    collection_manager = Controller()
    collection_manager.main()
