import tkinter as tk


class ToolBar(tk.Frame):
    def __init__(self, *args, **kwargs):
        self.master = kwargs['master']

        kwargs.update({
            'bd': 1,
            'relief': tk.RAISED,
        })
        super().__init__(*args, **kwargs)

        histogram_button = tk.Button(self, relief=tk.RAISED, text='Histogram', command=None)
        histogram_button.pack(side=tk.LEFT, padx=2, pady=2)
        self.pack(side=tk.TOP, fill=tk.X)
