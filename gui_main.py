import tkinter as tk


class gui:
    def __init__(self):
        self.main = tk.Tk()
        self.main.title('pip++')

        self.show_bag = tk.Button(text='刷新列表')
        self.show_bag.bind()

    def show(self) -> None:
        self.show_bag.grid(row=0, column=0, columnspan=2, rowspan=1, sticky='N+W+W+E ')
        self.tk.mainloop()
