import datetime
import tkinter as tk
from operator import truediv

import customtkinter


#UI elements
def greeting():
    now = datetime.datetime.now().time()
    if datetime.time(0, 0) <= now <= datetime.time(11, 59):
        greeting = "Good morning, how can I help you?"
    elif datetime.time(12, 0) <= now <= datetime.time(16, 59):
        greeting = "Good afternoon, how can I help you?"
    else:
        greeting = "Good evening, how can I help you?"
    return greeting

class Menu(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.option_1 = customtkinter.CTkButton(self, text="New Project...")
        self.option_1.grid(row=0, column=0, padx=10, pady=10, sticky= "ew")

        self.option_2 = customtkinter.CTkButton(self, text="Open...")
        self.option_2.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.option_3 = customtkinter.CTkButton(self, text="Save as...")
        self.option_3.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.option_4 = customtkinter.CTkButton(self, text="Settings")
        self.option_4.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

class Workbench(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)





class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Mapping Assistant")
        self.geometry("720x480")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.menu = Menu(self)
        self.menu.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.workbench = Workbench(self)
        self.workbench.grid(row=0, column=1, columnspan=2, padx=10, pady=10, sticky=tk.W)

#title = customtkinter.CTkLabel(app, text = greeting() )
#title.pack(padx = 5, pady = 5)

#file input- tkinter.filedialog

app = App()
app.mainloop()
