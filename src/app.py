import customtkinter
import tkinter as tk
from src.config import DEFAULT_PADX, DEFAULT_PADY, STICKY_NSEW
from src.menu import Menu
from src.views import Workbench, MapView, DataView

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Mapping Assistant")
        self.minsize(1680, 1050)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0,weight=1)

        self.workbench = Workbench(self)
        self.workbench.grid(row=0, column=0,padx=DEFAULT_PADX, pady=DEFAULT_PADY, sticky=STICKY_NSEW)

