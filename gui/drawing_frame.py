import os
import tkinter as tk
from copy import copy
from tkinter import filedialog

from PIL import ImageTk, Image
from pympler import muppy

from gui.histogram import Histogram
from gui.status_bar import StatusBar
from gui.toolbar import ToolBar
from image_processing.filters import FastBlur


class DrawingFrame(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters = self.get_filters()
        self.master = kwargs.get('master')
        self.width = self.master.width
        self.height = self.master.height

        self.image = None
        self.image_thumbnail = None

        self.pack()
        self.init_gui()

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
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.master.quit)
        self.menu_bar.add_cascade(label="File", menu=file_menu)

        edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        edit_menu.add_command(label="Fast Blur", command=self.apply_filter)
        edit_menu.add_command(label="Copy", command=None)
        edit_menu.add_command(label="Paste", command=None)
        self.menu_bar.add_cascade(label="Filters", menu=edit_menu)

        self.master.config(menu=self.menu_bar)

    def init_canvas(self):
        self.canvas_width = self.width
        self.canvas_height = self.height - 90
        self.canvas = tk.Canvas(master=self, width=self.canvas_width, height=self.canvas_height)
        self.canvas.create_rectangle(0, 0, self.width, self.height, fill='#7f7f7f')
        self.canvas.pack()

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
                ("all files", "*.*"),
                ("jpeg files", "*.jpg"),
                ("png files", "*.png"),
                ("bmp files", "*.bmp"),
            )
        )
        if path:
            self.set_pil_image(path)
            self.place_image_on_canvas(self.image)

    def save_file(self):
        path = filedialog.asksaveasfilename(
            initialdir='.',
            defaultextension=".jpg",
            title="Save File",
            filetypes=(
                ("all files", "*.*"),
                ("jpeg files", "*.jpg"),
                ("png files", "*.png"),
                ("bmp files", "*.bmp"),
            )
        )
        if path:
            self.image.save(path)

    def place_image_on_canvas(self, image=None):
        self.image_thumbnail = copy(image)
        self.image_thumbnail.thumbnail(size=(self.canvas_width - 100, self.canvas_height - 100))

        image = ImageTk.PhotoImage(image=self.image_thumbnail)
        self.canvas.image = image

        self.canvas.create_image(self.canvas_width / 2, self.canvas_height / 2, anchor=tk.CENTER, image=image)

        self.status_bar.update_status_bar(
            width=image.width(),
            height=image.height(),
            size=self.get_image_size(),
            ram=self.get_ram_usage()
        )

    def get_image_size(self):
        size = os.stat(self.image.filename).st_size
        return round(size // 1024)

    def get_ram_usage(self):
        return muppy.get_size(muppy.get_objects(include_frames=True)) // 1024

    def update_status_bar(self, width=None, height=None):
        self.status_bar.update_status_bar(
            width=width,
            height=height,
            ram=self.get_ram_usage()
        )

    def apply_filter(self, filter_name):
        filter_ = self.filters[filter_name]
        filtered_image = filter_.apply(self.image)
        self.place_image_on_canvas(image=filtered_image)

    def get_filters(self):
        return {
            'fast_blur': FastBlur
        }

    def set_pil_image(self, path):
        self.image = Image.open(path)
