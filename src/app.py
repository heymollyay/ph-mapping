import customtkinter
import tkinter as tk
from src.config import DEFAULT_PADX, DEFAULT_PADY, STICKY_NSEW
from src.menu import Menu
from src.views import Workbench, MapView, DataView

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Mapping Assistant")
        #self.geometry("820x580")
        self.columnconfigure((0,1), weight=1)
        self.rowconfigure((0,1), weight=1)

        self.menu = Menu(self)
        self.menu.grid(row=0, column=0, rowspan=2, padx=DEFAULT_PADX, pady=DEFAULT_PADY, sticky=STICKY_NSEW)

        self.workbench = Workbench(self)
        self.workbench.grid(row=0, column=1, rowspan=2,padx=DEFAULT_PADX, pady=DEFAULT_PADY, sticky=STICKY_NSEW)

