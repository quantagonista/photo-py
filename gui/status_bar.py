import tkinter as tk


class StatusBarLabel(tk.Label):
    def __init__(self, master, text_variable, *args, **kwargs):
        super().__init__(
            master=master, textvariable=text_variable, bd=1, width=30, relief=tk.SUNKEN, *args, **kwargs
        )


class StatusBar(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.width = tk.StringVar()
        self.height = tk.StringVar()
        self.image_size = tk.StringVar()
        self.ram_amount = tk.StringVar()

        self.width.set('W: 200')
        self.height.set('H: 400')
        self.image_size.set('Size:16 mb')
        self.ram_amount.set('RAM:120 mb')

        self.width_label = StatusBarLabel(master, self.width)
        self.height_label = StatusBarLabel(master, self.height)
        self.image_size_label = StatusBarLabel(master, self.image_size)
        self.ram_amount_label = StatusBarLabel(master, self.ram_amount)

        self.width_label.pack(side=tk.LEFT)
        self.height_label.pack(side=tk.LEFT)
        self.image_size_label.pack(side=tk.LEFT)
        self.ram_amount_label.pack(side=tk.LEFT)
        self.pack(fill=tk.X)

    def update_status_bar(self, width=None, height=None, size=None, ram=None):
        if width:
            self.width.set('W: {}'.format(width))

        if height:
            self.height.set('H: {}'.format(height))

        if size:
            self.image_size.set('Size: {}'.format(size))

        if ram:
            self.ram_amount.set('RAM: {}'.format(ram))
