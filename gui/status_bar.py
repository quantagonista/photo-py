import tkinter as tk


class StatusBarLabel(tk.Label):
    def __init__(self, *args, **kwargs):
        kwargs.update({
            'width': 40,
            'relief': tk.SUNKEN,
            'bd': 1,
        })
        super().__init__(*args, **kwargs)


class StatusBar(tk.Frame):
    def __init__(self, *args, **kwargs):
        master = kwargs['master']
        kwargs['width'] = master.width
        super().__init__(*args, **kwargs)

        self.width_value = tk.StringVar(master=self)
        self.height_value = tk.StringVar(master=self)
        self.image_size_value = tk.StringVar(master=self)
        self.ram_amount_value = tk.StringVar(master=self)

        self.width_value.set('W: 200')
        self.height_value.set('H: 400')
        self.image_size_value.set('Size:16 mb')
        self.ram_amount_value.set('RAM:120 mb')

        self.width_label = StatusBarLabel(master=self, textvariable=self.width_value)
        self.height_label = StatusBarLabel(master=self, textvariable=self.height_value)
        self.image_size_label = StatusBarLabel(master=self, textvariable=self.image_size_value)
        self.ram_amount_label = StatusBarLabel(master=self, textvariable=self.ram_amount_value)

        self.width_label.pack(side=tk.LEFT)
        self.height_label.pack(side=tk.LEFT)
        self.image_size_label.pack(side=tk.LEFT)
        self.ram_amount_label.pack(side=tk.LEFT)
        self.pack(side=tk.BOTTOM, fill=tk.X)

    def update_status_bar(self, width=None, height=None, size=None, ram=None):
        if width:
            self.width_value.set('W: {}'.format(width))

        if height:
            self.height_value.set('H: {}'.format(height))

        if size:
            self.image_size_value.set('Size: {}'.format(size))

        if ram:
            self.ram_amount_value.set('RAM: {}'.format(ram))
