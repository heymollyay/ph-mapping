import customtkinter
import tkinter as tk
from src.config import NEW_PROJECT_TITLE, OPEN_TITLE, SAVE_TITLE, SETTINGS_TITLE, HELP_TITLE, DEFAULT_PADY, DEFAULT_PADX, STICKY_NSEW, STICKY_W
from toplevels import *

class Menu(customtkinter.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        #Dictionary for storing toplevel window instances
        self.windows = {}

        #make sure to configure grid row/columns for frames as well so they change size
        self.grid_rowconfigure((0,1,2,3,4), weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.option_1 = customtkinter.CTkButton(self, text=NEW_PROJECT_TITLE, command=lambda: self.open_TopLevel('new_project_window', NewProjectTopLevel))
        self.option_1.grid(row=0, column=0, padx=DEFAULT_PADX, pady=DEFAULT_PADY, sticky=STICKY_NSEW)

        self.option_2 = customtkinter.CTkButton(self, text=OPEN_TITLE, command=lambda: self.open_TopLevel('open_project_window', OpenTopLevel))
        self.option_2.grid(row=1, column=0, padx=DEFAULT_PADX, pady=DEFAULT_PADY, sticky=STICKY_NSEW)

        self.option_3 = customtkinter.CTkButton(self, text=SAVE_TITLE, command=lambda: self.open_TopLevel('save_project_window', SaveTopLevel))
        self.option_3.grid(row=2, column=0, padx=DEFAULT_PADX, pady=DEFAULT_PADY, sticky=STICKY_NSEW)

        self.option_4 = customtkinter.CTkButton(self, text=SETTINGS_TITLE, command=lambda: self.open_TopLevel('settings_window', SettingsTopLevel))
        self.option_4.grid(row=3, column=0, padx=DEFAULT_PADX, pady=DEFAULT_PADY, sticky=STICKY_NSEW)

        self.option_5 = customtkinter.CTkButton(self, text=HELP_TITLE, command=lambda: self.open_TopLevel('help_window', HelpToplevel))
        self.option_5.grid(row=4, column=0, padx=DEFAULT_PADX, pady=DEFAULT_PADY, sticky=STICKY_NSEW)


    def open_TopLevel(self, window_key, window_class):

        if window_key not in self.windows or not self.windows[window_key].winfo_exists():
            self.windows[window_key] = window_class(self, self.master.workbench)
            self.windows[window_key].attributes('-topmost', True)
            self.windows[window_key].protocol('WM_DELETE_WINDOW', lambda: self.windows[window_key].destroy())
        else:
            self.windows[window_key].focus()