import tkinter as tk
from tkinter import ttk

from app.utils.helpers import LoadIcon

class Empty:
    def __init__(self, root):
        self.root = root
        self.root.title("Explorador de pasta de arquivos")
        logo_icon = LoadIcon("app/images/")
        self.root.iconphoto(False, logo_icon)


