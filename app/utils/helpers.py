import os
from PIL import Image, ImageTk

def LoadIcon(path):
    icon = Image.open(path)
    icon = icon.resize((16, 16), Image.LANCZOS)  
    return ImageTk.PhotoImage(icon)



def CreateNewName(file_name,tag_name):
    file_name, extensao = os.path.splitext(file_name)
    return f"{file_name}{tag_name}{extensao}"