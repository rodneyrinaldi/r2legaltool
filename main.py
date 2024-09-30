import shutil
import sys
import os
import argparse
import ctypes
import tkinter as tk


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

sys.path.append(os.path.join(os.path.dirname(__file__), 'forms'))

from app.utils.system import relocate_and_delete_self
parser = argparse.ArgumentParser(description="Script Installer")
parser.add_argument('--install', action='store_true', help="Install the script to the system's program directory")
args = parser.parse_args()
if args.install:
    if is_admin():
        relocate_and_delete_self()
        sys.exit("Instalação encerrada com êxito")
    sys.exit("Falta permissção de administrador")
else:
    from app.main_form import MainForm
    if __name__ == "__main__":
        root = tk.Tk()
        app = MainForm(root)
        root.mainloop()


    
