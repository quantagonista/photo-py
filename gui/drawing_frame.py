import math
import os
import tkinter as tk
from tkinter import filedialog

from PIL import ImageTk, Image
from pympler import muppy

from gui.histogram import Histogram
from gui.status_bar import StatusBar
from gui.toolbar import ToolBar


class DrawingFrame(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.master = kwargs.get('master')
        self.width = self.master.width
        self.height = self.master.height

        self.init_gui()
        self.pack()

    def init_gui(self):
        self.init_menu_bar()
        self.init_toolbar()
        self.init_canvas()
        self.init_status_bar()
        self.update_status_bar()

    def init_menu_bar(self):
        self.menu_bar = tk.Menu(self)

        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=None)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.master.quit)
        self.menu_bar.add_cascade(label="File", menu=file_menu)

        edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        edit_menu.add_command(label="Cut", command=None)
        edit_menu.add_command(label="Copy", command=None)
        edit_menu.add_command(label="Paste", command=None)
        self.menu_bar.add_cascade(label="Edit", menu=edit_menu)

        help_menu = tk.Menu(self.menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=None)
        self.menu_bar.add_cascade(label="Help", menu=help_menu)

        self.master.config(menu=self.menu_bar)

    def init_canvas(self):
        canvas_width = self.width
        canvas_height = self.height - 90
        self.canvas = tk.Canvas(self, width=canvas_width, height=canvas_height)
        self.canvas.create_rectangle(0, 0, self.width, self.height, fill='#7f7f7f')
        self.canvas.pack(expand=tk.YES)

    def init_toolbar(self):
        self.tool_bar = ToolBar(master=self)

    def init_status_bar(self):
        self.status_bar = StatusBar(master=self)

    def show_histogram(self):
        self.histogram.show()

    def init_histogram(self):
        self.histogram = Histogram(master=self.master, in_=self)

    def init_history_panel(self):
        pass

    def open_file(self):
        path = filedialog.askopenfilename(
            initialdir='.',
            defaultextension=".png",
            title="Open File",
            filetypes=(
                ("jpeg files", "*.jpg"),
                ("png files", "*.png"),
                ("bmp files", "*.bmp"),
            )
        )
        if path:
            self.place_image_on_canvas(path)

    def place_image_on_canvas(self, path='adventure-climb-conifer-640781.jpg'):
        image_file = Image.open(path)
        image = ImageTk.PhotoImage(image=image_file)

        self.canvas.create_image(0, 0, image=image, anchor=tk.NW)

        self.status_bar.update_status_bar(
            width=image.width(),
            height=image.height(),
            size=self.get_image_size(path),
            ram=self.get_ram_usage()
        )

    def get_image_size(self, path):
        size = os.stat(path).st_size
        return round(size // 1024)

    def get_ram_usage(self):
        return muppy.get_size(muppy.get_objects(include_frames=True)) // 1024

    def update_status_bar(self, width=None, height=None):
        self.status_bar.update_status_bar(
            width=width,
            height=height,
            ram=self.get_ram_usage()
        )
