import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'forms'))

import tkinter as tk
from gui.main_form import MainForm

if __name__ == "__main__":
    root = tk.Tk()
    app = MainForm(root)
    root.mainloop()
