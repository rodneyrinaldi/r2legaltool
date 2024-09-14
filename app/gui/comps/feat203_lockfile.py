import os
import time
import time
from datetime import datetime
import tkinter as Tk
from tkinter import  filedialog
import pymupdf
from PyPDF2 import PdfReader, PdfWriter

from utils.helpers import CreateNewName


def LockerFile(input_filename,u_password,o_password):
    output_filename = CreateNewName(input_filename,"(prot)")

    permission = 4 #PRINT constant permission
    reader = PdfReader(input_filename)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    writer.encrypt(user_password=u_password, owner_password=o_password,permissions_flag=permission)

    with open(output_filename, "wb") as output_file:
        writer.write(output_filename)
    writer.close()

    return(output_filename)