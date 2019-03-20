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

        self.place()

    def show(self):
        self.visible = not self.visible
        self.lower() if not self.visible else self.lift()

    def place(self):
        self.overrideredirect(1)
        self.lower()
        self.geometry('{w}x{h}+{x}+{y}'.format(
            w=self.width,
            h=self.height,
            x=500,
            y=0,
        ))
