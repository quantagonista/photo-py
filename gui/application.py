import tkinter as tk

from gui.drawing_frame import DrawingFrame
from gui.histogram import Histogram


class PhotoPy(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.width = self.winfo_screenwidth() - 50
        self.height = self.winfo_screenheight() - 50
        self.geometry('{w}x{h}'.format(w=self.width, h=self.height))
        self.attributes('-fullscreen', True)
        self.resizable(False, False)
        self.title('PHOTOPY')

        self.drawing_frame = DrawingFrame(master=self)
        self.histogram = Histogram(master=self)
        self.history_panel = None
