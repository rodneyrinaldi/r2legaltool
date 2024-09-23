import time
from datetime import date
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog

from app.utils.helpers import LoadIcon
from app.processing.feat203_lockfile import LockerFile


class OabTable:
    def __init__(self, root):
        return