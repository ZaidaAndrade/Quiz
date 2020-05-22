import os
import shutil
import hashlib
from tkinter import Tk, Menu, Toplevel, LabelFrame, Label, Entry, Button, messagebox
from tkinter.ttk import Combobox, Style
from tkinter.constants import *
from datetime import datetime
from Config.Visual import *

from frm_quiz import FormParentQuiz

# root = Tk()
# root.mainloop()


class WindowHome:
    def __init__(self):
        #
        # Configuration of the window

        self.role = 1
        self.root = Tk()
        # self.window.protocol("WM_DELETE_WINDOW", self.click_log_out)
        # w, h = self.window.winfo_screenwidth(), self.window.winfo_screenheight()
        # self.window.geometry('%dx%d+0+0' % (1024, 778))
        # self.window.geometry('%dx%d+0+0' % (1500, 778))
        # self.window.geometry('%dx%d+0+0' % (w, h))
        # Place window on top left corner
        self.root.geometry('+%d+%d' % (0, 0))
        self.root.resizable(0, 0)
        self.root.title('Tool for experimenting')
        self.root.withdraw()
        # self.create_login()
        # self.show_login()
        self.access_system()


    def access_system(self):
        # Components (tool bar) will be shown depending on the role of the user

        self.frm_parent_quiz= FormParentQuiz(self.root)
        self.frm_parent_quiz.show_frm()
        self.root.deiconify()


        # menu_bar = Menu(self.window)
        # self.window.config(menu=menu_bar)

app = WindowHome()
app.root.mainloop()


