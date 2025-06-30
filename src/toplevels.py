import customtkinter
import tkinter as tk
from src.config import NEW_PROJECT_TITLE, OPEN_TITLE, SAVE_TITLE, SETTINGS_TITLE, HELP_TITLE, DEFAULT_PADY, DEFAULT_PADX, STICKY_NSEW, STICKY_W
from src.views import Workbench


class CustomTopLevel(customtkinter.CTkToplevel):
    def __init__(self, title, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title(title)
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)


class NewProjectTopLevel(CustomTopLevel):
   def __init__(self, master, workbench, *args, **kwargs):
        super().__init__(title=NEW_PROJECT_TITLE)
        self.workbench = workbench

        self.label = customtkinter.CTkLabel(self,text=NEW_PROJECT_TITLE)
        self.label.grid(column=0, row=0, padx = DEFAULT_PADX, pady = DEFAULT_PADY, sticky=STICKY_NSEW)

        new_project_name = tk.StringVar(self)
        self.name_entry = customtkinter.CTkEntry(self, placeholder_text="Name",textvariable=new_project_name)
        self.name_entry.grid(column=1, row=0, padx = DEFAULT_PADX, pady = DEFAULT_PADY, sticky=STICKY_W)

        self.button_ok = customtkinter.CTkButton(self, text = "Ok", command=self.create_project)
        self.button_ok.grid(column=0, row=1, padx = DEFAULT_PADX, pady = DEFAULT_PADY, sticky=STICKY_W)
        self.button_cancel = customtkinter.CTkButton(self, text = "Cancel", command=self.destroy)
        self.button_cancel.grid(column=1, row=1, padx = DEFAULT_PADX, pady = DEFAULT_PADY, sticky=STICKY_W)


   def create_project(self):
        name = self.name_entry.get()
        if name:
            self.workbench.add_new_tab(name)
            self.destroy()

class OpenTopLevel(CustomTopLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(title=OPEN_TITLE)


class SaveTopLevel(CustomTopLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(title=SAVE_TITLE)

class SettingsTopLevel(CustomTopLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(title=SETTINGS_TITLE)


class HelpToplevel(CustomTopLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(title=HELP_TITLE)
