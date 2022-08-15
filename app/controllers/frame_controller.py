from tkinter import *
from tkinter import ttk


class FrameController:

    def __init__(self, root):

        self.frm = ttk.Frame(root, padding=10)
        self.frm.grid()
        ttk.Label(self.frm, text="Hello World!").grid(column=0, row=0)
        ttk.Button(self.frm, text="Quit", command=root.destroy).grid(column=1, row=0)

