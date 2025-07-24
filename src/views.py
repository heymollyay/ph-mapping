import os
import customtkinter
import tkinter as tk
import openpyxl
from tkinter import filedialog, ttk
from src.config import NEW_PROJECT_TITLE, STICKY_NSEW, DEFAULT_PADX, DEFAULT_PADY
from src.dataview import DataView


class MapView(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

class AssistantView(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

class Workbench(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # Dictionary for each tab
        self.tab_views = {}

        #Default tab on entry
        self.add_new_tab(NEW_PROJECT_TITLE)

    def add_new_tab(self, name):
        if name:
            self.add(name)
            self.set(name)

            #frame within the tab
            container = customtkinter.CTkFrame(self.tab(name))
            container.pack(fill="both", expand=1)
            container.grid_rowconfigure((0,1), weight=1)
            container.grid_columnconfigure((0,1), weight=1)

            assistant_view = AssistantView(container)
            assistant_view.grid(row=0, column=0, rowspan=2, sticky = STICKY_NSEW)
            map_view = MapView(container)
            map_view.grid(row=0, column=1, padx= DEFAULT_PADX, pady=DEFAULT_PADY, sticky = STICKY_NSEW)
            data_view = DataView(container)
            data_view.grid(row=1,column=1,padx=DEFAULT_PADX,pady=DEFAULT_PADY,sticky=STICKY_NSEW)

            self.tab_views[name] = {"map_view": map_view, "data_view": data_view, "assistant_view": assistant_view}



