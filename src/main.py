import customtkinter
from src.app import App

if __name__ == '__main__':
    customtkinter.set_appearance_mode("System")
    app = App()
    app.mainloop()