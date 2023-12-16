import tkinter as tk
import tkinter.messagebox
import threading
import pip_operation
import config

if config.use_source_test:
    import source_test

    Image_source = source_test.Image_source_dict_new
else:
    Image_source = config.Image_source_dict


class gui:
    def __init__(self):
        self.main = tk.Tk()
        self.main.title('pip++')

        self.show_library = tk.Button(text='刷新列表')
        self.show_list = tk.Listbox()
        self.show_library.bind('<Button-1>', self.list_dispose())

        self.install_library_name = tk.Entry()
        self.install_library_button = tk.Button(text='下载包', command=self.install_dispose)

        self.install_library_list = tk.Listbox()
        for item in Image_source.keys():
            self.install_library_list.insert("end", item)

    def install_dispose(self):
        name = self.install_library_name.get()
        source = config.Image_source_dict[self.install_library_list.get(self.install_library_list.curselection())]
        if name == '':
            tk.messagebox.showerror('pip++', '请输入包名')
            return
        install = threading.Thread(target=pip_operation.pip_install, daemon=True, args=[name, True, source])
        install.start()

    def list_dispose(self):
        self.show_list.select_clear(0, self.show_list.size())
        bag_list = pip_operation.pip_list()
        for x in bag_list:
            self.show_list.insert(tk.END, x)

    def show(self) -> None:
        self.show_library.grid(row=0, column=0, columnspan=2, rowspan=2, sticky=tk.NSEW)
        self.show_list.grid(row=2, column=0, columnspan=2, rowspan=2, sticky=tk.NSEW)

        self.install_library_button.grid(row=0, column=3, columnspan=1, rowspan=2, sticky=tk.NSEW)
        self.install_library_name.grid(row=0, column=4, columnspan=1, rowspan=2, sticky=tk.NSEW)
        self.install_library_list.grid(row=2, column=3, columnspan=2, rowspan=2, sticky=tk.NSEW)

        self.main.mainloop()
