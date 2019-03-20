import tkinter as tk


class Histogram(tk.Toplevel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.visible = False
        self.width = 200
        self.height = 150
        self.master = kwargs['master']
        self.canvas = tk.Canvas(master=self)
        self.canvas.create_rectangle(0, 0, self.width, self.height, fill='yellow')
        self.canvas.place(x=self.master.width, y=50)
        self.resizable(False, False)

    def show(self):
        self.visible = not self.visible
        self.lower() if not self.visible else self.lift()
