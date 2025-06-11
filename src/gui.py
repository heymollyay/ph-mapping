import tkinter as tk
from tkinter import *
import datetime

#Setup
gui = tk.Tk()
gui.title('Assistant')
gui.geometry('500x300')

#Menu
menu = Menu(gui)
gui.config(menu=menu)
filemenu =Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New...')
filemenu.add_command(label='Open...')
filemenu.add_command(label='Save as...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=gui.quit)

helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')
helpmenu.add_command(label='Tutorial')


#Greeting
now = datetime.datetime.now().time()
if datetime.time(0,0) <= now <= datetime.time(11, 59):
    greeting = "Good morning, how can I help you?"
elif datetime.time(12,0) <= now <= datetime.time(16, 59):
    greeting = "Good afternoon, how can I help you?"
else:
    greeting = "Good evening, how can I help you?"

messageBox = Message(master = gui, text = greeting)
messageBox.config(bg="white")
messageBox.pack()

#Options
optionNew = tk.Button(gui, text='New project', width = 25)
optionNew.config(bg="white")
optionOpen = tk.Button(gui, text='Open', width = 25)
optionOpen.config(bg="white")
optionNew.pack()
optionOpen.pack()

gui.mainloop()
