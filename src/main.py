import datetime
import tkinter as tk
from operator import truediv

import customtkinter
from customtkinter import CTkToplevel

class NewProjectTopLevel(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("New Project")
        self.resizable(False, False)

        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure((0,1), weight=1)

        self.label = customtkinter.CTkLabel(self,text="New Project: ")
        self.label.grid(column=0, row=0, padx =10,pady=10, sticky='NESW')

        new_project_name = tk.StringVar(self)
        self.name_entry = customtkinter.CTkEntry(self, placeholder_text="Name",textvariable=new_project_name)
        self.name_entry.grid(column=1, row=0,padx =10,pady=10, sticky='w')

        self.button_ok = customtkinter.CTkButton(self, text = "Ok")
        self.button_ok.grid(column=0, row=1,padx =10,pady=10, sticky='W')
        self.button_cancel = customtkinter.CTkButton(self, text = "Cancel")
        self.button_cancel.grid(column=1, row=1,padx =10, pady=10, sticky='W')

class Menu(customtkinter.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        #make sure to configure grid row/columns for frames as well so they change size
        self.grid_rowconfigure((0,1,2,3,4), weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.option_1 = customtkinter.CTkButton(self, text="New Project...", command=self.open_new_project_window)
        self.option_1.grid(row=0, column=0, padx=10, pady=10, sticky=tk.NSEW)

        self.option_2 = customtkinter.CTkButton(self, text="Open...")
        self.option_2.grid(row=1, column=0, padx=10, pady=10, sticky=tk.NSEW)

        self.option_3 = customtkinter.CTkButton(self, text="Save...")
        self.option_3.grid(row=2, column=0, padx=10, pady=10, sticky=tk.NSEW)

        self.option_4 = customtkinter.CTkButton(self, text="Settings")
        self.option_4.grid(row=3, column=0, padx=10, pady=10, sticky=tk.NSEW)

        self.option_5 = customtkinter.CTkButton(self, text="Help")
        self.option_5.grid(row=4, column=0, padx=10, pady=10, sticky=tk.NSEW)

        self.new_project_window = None

    def open_new_project_window(self):
        if self.new_project_window is None or not self.new_project_window.winfo_exists():
            self.new_project_window = NewProjectTopLevel(self)
            self.new_project_window.attributes('-topmost', True)
        else:
            self.new_project_window.focus()



class Workbench(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.add("New")



        #Add new tab if new project is created

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
        #self.geometry("820x580")
        self.columnconfigure((0,1), weight=1)
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
