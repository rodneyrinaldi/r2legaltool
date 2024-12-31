import os
import traceback
import tkinter as Tk
from tkinter import filedialog

from app.processing.feat202_tagfile import LabelerFile


def RegisterFile(secure_key, input_filename, print_page_numbers=False, decrease=False, a4format=False, protect=False, zip=False):
    LabelerFile(secure_key, None, None, input_filename, None, print_page_numbers, decrease, a4format, protect, zip)
    return    