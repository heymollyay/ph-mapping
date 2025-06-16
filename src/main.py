import datetime
import tkinter as tk
from operator import truediv

import customtkinter

class Menu(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        #make sure to configure grid row/columns for frames as well so they change size
        self.grid_rowconfigure((0,1,2,3), weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.option_1 = customtkinter.CTkButton(self, text="New Project...")
        self.option_1.grid(row=0, column=0, padx=10, pady=10, sticky=tk.NSEW)

        self.option_2 = customtkinter.CTkButton(self, text="Open...")
        self.option_2.grid(row=1, column=0, padx=10, pady=10, sticky=tk.NSEW)

        self.option_3 = customtkinter.CTkButton(self, text="Save as...")
        self.option_3.grid(row=2, column=0, padx=10, pady=10, sticky=tk.NSEW)

        self.option_4 = customtkinter.CTkButton(self, text="Settings")
        self.option_4.grid(row=3, column=0, padx=10, pady=10, sticky=tk.NSEW)

class Workbench(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.add("New")
        #Add new tab if new project is created
        open_greeting = "Welcome to PH Mapping. How can I assist you today?"
        self.message = customtkinter.CTkLabel(self, text=open_greeting)
        self.message.grid(row=0, column=0, padx=10, pady=10, sticky=tk.NSEW)

class MapView(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)


class DataView(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Mapping Assistant")
        self.geometry("820x580")
        self.columnconfigure((0,1,2), weight=1)
        self.rowconfigure((0,1), weight=1)


        self.menu = Menu(self)
        self.menu.grid(row=0, column=0, rowspan=2, padx=10, pady=10, sticky=tk.NSEW)

        self.workbench = Workbench(self)
        self.workbench.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky=tk.NSEW)

        self.mapview = MapView(self)
        self.mapview.grid(row=0, column=2, padx=10, pady=10, sticky=tk.NSEW)

        self.dataview = DataView(self)
        self.dataview.grid(row=1, column=2, padx=10, pady=10, sticky=tk.NSEW)


#title = customtkinter.CTkLabel(app, text = greeting() )
#title.pack(padx = 5, pady = 5)

#file input- tkinter.filedialog

app = App()
app.mainloop()
