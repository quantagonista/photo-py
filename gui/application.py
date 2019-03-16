import tkinter as tk

from gui.status_bar import StatusBar


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.width = self.parent.winfo_screenwidth()
        self.height = self.parent.winfo_screenheight()

        self.init_gui()

    def init_gui(self):

        self.parent.geometry('{w}x{h}'.format(w=self.width, h=self.height))
        self.parent.resizable(False, False)
        self.init_menubar()
        self.init_canvas()
        self.init_history_panel()
        self.init_toolbar()
        self.init_status_bar()

    def init_menubar(self):
        self.menu_bar = tk.Menu(self.parent)

        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Open", command=None)
        file_menu.add_command(label="Save", command=None)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.parent.quit)
        self.menu_bar.add_cascade(label="File", menu=file_menu)

        edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        edit_menu.add_command(label="Cut", command=None)
        edit_menu.add_command(label="Copy", command=None)
        edit_menu.add_command(label="Paste", command=None)
        self.menu_bar.add_cascade(label="Edit", menu=edit_menu)

        help_menu = tk.Menu(self.menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=None)
        self.menu_bar.add_cascade(label="Help", menu=help_menu)

        self.parent.config(menu=self.menu_bar)

    def init_canvas(self):
        self.canvas = tk.Canvas(self.parent)
        self.canvas.create_rectangle(0, 0, self.width, self.height)
        self.canvas.pack(fill=tk.X)

    def init_history_panel(self):
        pass

    def init_toolbar(self):
        pass

    def init_status_bar(self):
        self.status_bar = StatusBar(self.parent)
