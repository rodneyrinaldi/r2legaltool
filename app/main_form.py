import tkinter as tk
from tkinter import Menu

from app.forms.child000_empty import Empty
from app.forms.child101_config import Config 
from app.forms.child102_folders import Folders
from app.forms.child103_tables import Tables
from app.forms.child104_processes import Processes
from app.forms.child201_regfile import RegFile
from app.forms.child202_tagfile import TagFile
from app.forms.child203_lockfile import LockFile
from app.forms.child204_oabtable import OabTable
from app.forms.child301_signfile import SignFile

from app.utils.helpers import LoadIcon

class MainForm:
    def __init__(self, root):
        self.root = root
        self.control_name = None
        self.root.title("R2 Legal Tool")
        self.root.geometry("800x600")
        self.root.configure(bg="white")

        self.create_menu()
        self.create_mdi_area() 
        self.center_window(800,600)
        
        logo_icon = LoadIcon("../images/logo.png")
        self.root.iconphoto(False, logo_icon)

        mdi_bg_color = self.root.cget("bg")
        frame = tk.Frame(root, bg=mdi_bg_color)
        frame.place(relx=0.5, rely=0.5, anchor="center")
        self.label = tk.Label(frame, text="Controle não Selecionado", font=("Helvetica", 12), fg="black", bg=mdi_bg_color)
        self.label.pack()


    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2 - 30
        self.root.geometry(f"{width}x{height}+{x}+{y}")
       

    def create_menu(self):
        menu_bar = Menu(self.root)
        self.root.config(menu=menu_bar)

        file_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Sistema", menu=file_menu)
        file_menu.add_command(label="Configurador de perfil", command=self.open_child101_config,state="normal")
        file_menu.add_command(label="Explorador de pasta de arquivos", command=self.open_child102_folders,state="normal")
        file_menu.add_separator()        
        file_menu.add_command(label="Importador de tabela de honorários da OABSP", command=self.open_child103_oabtable,state="normal")
        file_menu.add_separator()
        file_menu.add_command(label="Importador de processos de do TJSP", command=self.open_child104_processes,state="normal")
        file_menu.add_separator()
        file_menu.add_command(label="Sair do sitema", command=self.root.quit)

        functions_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Recursos", menu=functions_menu)
        functions_menu.add_command(label="Registrador de documentos", command=self.open_child201_regfile)
        functions_menu.add_command(label="Etiquetador de documentos", command=self.open_child202_tagfile)
        functions_menu.add_command(label="Protetor de documentos", command=self.open_child203_lockfile)
        functions_menu.add_separator()
        functions_menu.add_command(label="Consultor de honorários OABSP", command=self.open_child204_oabtable,state="normal")
        functions_menu.add_separator()
        functions_menu.add_command(label="Consultor de instabilidade TJSP", command=self.open_child000_empty,state="disabled")
        functions_menu.add_command(label="Consultor de processos TJSP", command=self.open_child000_empty,state="disabled")
        functions_menu.add_command(label="Consultor de custas processuais TJSP", command=self.open_child000_empty,state="disabled")

        functions_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Recursos Avançados", menu=functions_menu)
        functions_menu.add_command(label="Assinador digital de documento", command=self.open_child301_signfile)
        functions_menu.add_separator()
        functions_menu.add_command(label="Gestor de processos TJSP", command=self.open_child000_empty,state="disabled")

    def create_mdi_area(self):
        self.mdi_area = tk.Frame(self.root, bg="white")
        self.mdi_area.pack(fill=tk.BOTH, expand=True)
        

    def open_child000_empty(self):
        self.root.attributes("-disabled", True)
        new_window = tk.Toplevel(self.mdi_area)
        self.center_child_window(new_window, 720,400)
        new_window.protocol("WM_DELETE_WINDOW", lambda: self.on_child_close(new_window))
        Empty(new_window)
        

    def open_child101_config(self):
        self.root.attributes("-disabled", True)
        new_window = tk.Toplevel(self.mdi_area)
        self.center_child_window(new_window, 720,400)
        new_window.protocol("WM_DELETE_WINDOW", lambda: self.on_child_close(new_window))
        Config(new_window)
        

    def open_child102_folders(self):
        self.root.attributes("-disabled", True)
        new_window = tk.Toplevel(self.mdi_area)
        self.center_child_window(new_window, 720,400)
        new_window.protocol("WM_DELETE_WINDOW", lambda: self.on_child_close(new_window))
        Folders(new_window)
        

    def open_child103_oabtable(self):
        self.root.attributes("-disabled", True)
        new_window = tk.Toplevel(self.mdi_area)
        self.center_child_window(new_window, 720,400)
        new_window.protocol("WM_DELETE_WINDOW", lambda: self.on_child_close(new_window))
        Tables(new_window)
        

    def open_child104_processes(self):
        self.root.attributes("-disabled", True)
        new_window = tk.Toplevel(self.mdi_area)
        self.center_child_window(new_window, 720,400)
        new_window.protocol("WM_DELETE_WINDOW", lambda: self.on_child_close(new_window))
        Tables(new_window)


    def open_child201_regfile(self):
        self.root.attributes("-disabled", True)
        new_window = tk.Toplevel(self.mdi_area)
        self.center_child_window(new_window, 720,400)
        new_window.protocol("WM_DELETE_WINDOW", lambda: self.on_child_close(new_window))
        RegFile(new_window)


    def open_child202_tagfile(self):
        self.root.attributes("-disabled", True)
        new_window = tk.Toplevel(self.mdi_area)
        self.center_child_window(new_window, 720,400)
        new_window.protocol("WM_DELETE_WINDOW", lambda: self.on_child_close(new_window))
        TagFile(new_window)


    def open_child203_lockfile(self):
        self.root.attributes("-disabled", True)
        new_window = tk.Toplevel(self.mdi_area)
        self.center_child_window(new_window, 720,400)
        new_window.protocol("WM_DELETE_WINDOW", lambda: self.on_child_close(new_window))
        LockFile(new_window)


    def open_child204_oabtable(self):
        self.root.attributes("-disabled", True)
        new_window = tk.Toplevel(self.mdi_area)
        self.center_child_window(new_window, 720,400)
        new_window.protocol("WM_DELETE_WINDOW", lambda: self.on_child_close(new_window))
        OabTable(new_window)


    def open_child301_signfile(self):
        self.root.attributes("-disabled", True)
        new_window = tk.Toplevel(self.mdi_area)
        self.center_child_window(new_window, 720,400)
        new_window.protocol("WM_DELETE_WINDOW", lambda: self.on_child_close(new_window))
        SignFile(new_window)


    def center_child_window(self, window, width, height):        
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2  - 30      
        window.geometry(f"{width}x{height}+{x}+{y}")
        window.transient(self.root)  
        window.grab_set()  


    def on_child_close(self, window):
        window.destroy()
        self.root.attributes("-disabled", False)
        self.root.focus_set()  
        self.root.lift()  