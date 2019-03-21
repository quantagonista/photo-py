import tkinter as tk


class ToolBar(tk.Frame):
    def __init__(self, *args, **kwargs):
        self.master = kwargs['master']

        kwargs.update({
            'bd': 1,
            'relief': tk.RAISED,
        })
        super().__init__(*args, **kwargs)

        histogram_button = tk.Button(self, relief=tk.RAISED, text='Histogram', command=self.show_histogram)
        histogram_button.pack(side=tk.LEFT, padx=2, pady=2)

        open_button = tk.Button(self, relief=tk.RAISED, text='Open file', command=self.master.place_image_on_canvas)
        open_button.pack(side=tk.LEFT, padx=2, pady=2)

        self.pack(side=tk.TOP, fill=tk.X)

    def show_histogram(self):
        self.master.master.histogram.show()
